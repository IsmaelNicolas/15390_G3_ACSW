from fastapi import (APIRouter, Depends, FastAPI, HTTPException, Response,
                     status)
from Utils.Crud import HistoriaCRUD
from Models.History import Historia, HistoriaCreate, HistoriaUpdate
from Models.User import User
from Utils.Services import current_user
from typing import List

router = APIRouter()

@router.post("/historias/", response_model=Historia)
def create_historia(historia_create: HistoriaCreate,user: User = Depends(current_user)):
    return HistoriaCRUD.create_historia(historia_create,user_id=user.user_id)

@router.get("/historias/{historia_id}", response_model=Historia)
def read_historia(historia_id: str,user: User = Depends(current_user)):
    historia = HistoriaCRUD.get_historia(historia_id)
    if historia:
        return historia
    raise HTTPException(status_code=404, detail="Historia not found")

@router.put("/historias/{historia_id}", response_model=Historia)
def update_historia(historia_id: str, historia_update: HistoriaUpdate,user: User = Depends(current_user)):
    historia = HistoriaCRUD.update_historia(historia_id, historia_update)
    if historia:
        return historia
    raise HTTPException(status_code=404, detail="Historia not found")

@router.delete("/historias/{historia_id}", response_model=None)
def delete_historia(historia_id: str,user: User = Depends(current_user)):
    HistoriaCRUD.delete_historia(historia_id)
    return None

@router.get("/api/historias", response_model=List[Historia] )
def read_all_historias(user: User = Depends(current_user)):
    historias = HistoriaCRUD.get_all_historias(user_id=user.user_id)
    return historias
