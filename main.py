from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
import uvicorn

MAX_File_SIZE = 20 * 1024 * 1024  
app = FastAPI()

@app.middleware("http")
async def limit_file_size(request: Request, call_next):
    content_length = request.headers.get('Content-Length')
    if content_length and int(content_length) > MAX_File_SIZE:
        return JSONResponse(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            content={"detail": "File size exceeds the maximum limit of 20MB."}
        )
    response = await call_next(request)
    return response

@app.get("/")
def read_root():
    return {"Hello": "World"}
