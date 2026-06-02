from pydantic import BaseModel, Field
from typing import List, Dict, Any

class CSVData(BaseModel):
    chunk_index: int = Field(..., description="Index of the current chunk of data")
    headers: List[str] = Field(..., description="List of column headers in the CSV file")
    rows: List[Dict[str, Any]] = Field(..., description="List of rows, where each row is a dictionary mapping header to value")

class CSVSchema(BaseModel):
    filename: str = Field(..., description="Name of the CSV file")
    chunks: List[CSVData] = Field(..., description="List of all chunks of data in the CSV file")
    encoding: str = Field(default="utf-8", description="Encoding of the CSV file")


class ExportRequest(BaseModel):
    filename: str = 'dados_editados.csv'
    encoding: str = 'utf-8'
    delimiter: str = ','
    chunks: List[CSVData]
