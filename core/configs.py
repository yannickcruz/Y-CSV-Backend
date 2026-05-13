from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Y-CSV-Server"
    version: str = "0.1.0"
    HOST: str = "0.0.0.0"
    PORT: int = 7056
    debug: bool = True