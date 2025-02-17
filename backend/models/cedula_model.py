from pydantic import BaseModel

class CedulaRequest(BaseModel):
    cedula: str