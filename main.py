from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from api.routers import csv_router
import uvicorn

app = FastAPI()
app.include_router(csv_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

MAX_File_SIZE = 20 * 1024 * 1024  

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
    return {"message": "Y-CSV API está rodando!"}
