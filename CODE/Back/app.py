import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.login import api_router
from router.user import api_router as user_router
from router.history import router as history_router
from Utils.Services import *

app = FastAPI()

"""
Configuración del CORS
Se definen los dominios permitidos para las solicitudes CORS.
"""
origins = [
    "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mis = 'hello'
ps = 'pt'

app.include_router(api_router)
app.include_router(user_router)
app.include_router(history_router)


if __name__ == "__main__":
    """
    Inicia el servidor uvicorn en el archivo "app" con la variable "app".
    Se configura el host en "0.0.0.0" para aceptar conexiones de cualquier dirección IP.
    Se configura el puerto en 8000.
    Se habilita el modo de recarga automática para el desarrollo.
    """
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)