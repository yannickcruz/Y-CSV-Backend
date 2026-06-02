import pandas as pd
import io

def csv_upload(buffer: io.BytesIO, chunk_rows: int = 100) -> dict:

    df_iterator = pd.read_csv(buffer, encoding='utf-8', chunksize=chunk_rows)

    payload = []
    for i, chunk in enumerate(df_iterator):
        chunk_data = {
            "chunk_index": i,
            "headers": chunk.columns.tolist(),
            "rows": chunk.to_dict(orient="records")
        }
        payload.append(chunk_data)

    return {
        "total_chunks": len(payload),
        "chunks": payload
    }

def csv_download(data: dict) -> bytes:
    
    output = io.StringIO()
    sorted_chunks = sorted(data["chunks"], key=lambda x: x["chunk_index"])

    for index, chunk in enumerate(sorted_chunks):
        df_chunk = pd.DataFrame(chunk["rows"])
        write_header = True if index == 0 else False

        df_chunk.to_csv(output, index=False, header=write_header)
    
    return output.getvalue().encode('utf-8')