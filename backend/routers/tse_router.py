from fastapi import APIRouter, HTTPException
from backend.models.cedula_model import CedulaRequest
from backend.services.tse_service import TSEService

router = APIRouter()

@router.get("/consulta/")
async def consultar_cedula(cedula: str):
    tse_service = TSEService()
    try:
        html_content = tse_service.obtener_informacion(cedula)
        if not html_content:
            raise HTTPException(status_code=404, detail="No se pudo obtener información de la cédula.")
        
        informacion = tse_service.extraer_informacion(html_content)
        if not informacion:
            raise HTTPException(status_code=404, detail="No se pudo extraer información correctamente.")
        
        return informacion
    finally:
        tse_service.cerrar()