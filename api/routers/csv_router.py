from schemas import csv_schema
from services.csv_service import csv_upload, csv_download
from fastapi import APIRouter, HTTPException, UploadFile, File, Response
from pathlib import Path
import io

router = APIRouter()

@router.get('/', response_model=csv_schema.CSVSchema)
async def get_csv_data():
    try:
        csv_data = {
            "filename": "example.csv",
            "chunks": [
                {
                    "chunk_index": 0,
                    "headers": ["id", "name", "age"],
                    "rows": [
                        {"id": 1, "name": "Alice", "age": 30},
                        {"id": 2, "name": "Bob", "age": 25}
                    ]
                }
            ],
            "encoding": "utf-8"
        }
        return csv_schema.CSVSchema(**csv_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/upload', response_model=csv_schema.CSVSchema)
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        filename_end = Path(file.filename).suffix
        raise HTTPException(status_code=400, detail="O arquivo deve ser um CSV. O arquivo enviado é um: " + filename_end)
    try:
        contents = await file.read()
        buffer = io.BytesIO(contents)
        result_json = csv_upload(buffer, chunk_rows=100)
        return {
            "filename": file.filename,
            "chunks": result_json["chunks"],
            "encoding": "utf-8"
        }
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="Erro de decodificação. Certifique-se de que o arquivo está codificado em UTF-8.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/download')
async def download_csv(request: csv_schema.ExportRequest):
    try:
        payload_dict = request.model_dump()
        csv_bytes = csv_download(payload_dict)
        headers = {
            "Content-Disposition": f'attachment; filename="{request.filename}"',
        }
        return Response(content=csv_bytes, media_type="text/csv", headers=headers)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))