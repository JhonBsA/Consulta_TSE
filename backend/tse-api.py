from fastapi import FastAPI
from backend.routers import tse_router

app = FastAPI()
app.include_router(tse_router.router, prefix="/tse", tags=["Consulta TSE"])

@app.get("/")
def read_root():
    return {"message": "API del TSE funcionando"}