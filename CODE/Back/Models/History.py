from typing import Optional
from datetime import datetime
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

    class Config:
        orm_mode = True
