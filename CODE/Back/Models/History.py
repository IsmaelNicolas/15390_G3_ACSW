from typing import Annotated, Optional
from datetime import datetime
from fastapi import File, UploadFile
from pydantic import BaseModel

class HistoriaBase(BaseModel):
    fecha: datetime
    intensidad: str
    blanco_biologico: str

class HistoriaCreate(HistoriaBase):
    pass

class HistoriaUpdate(BaseModel):
    fecha: Optional[datetime]
    intensidad: Optional[str]
    blanco_biologico: Optional[str]

class Historia(HistoriaBase):
    id: str
    imageURL: Optional[str]  # Asegúrate de que imageURL sea opcional si algunos documentos no lo tienen

    class Config:
        orm_mode = True

