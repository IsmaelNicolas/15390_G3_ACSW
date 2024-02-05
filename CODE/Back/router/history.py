import os
from bson.objectid import ObjectId
from fastapi import (APIRouter, Depends, FastAPI, File, HTTPException, Response, UploadFile,
                     status)
from Utils.Crud import HistoriaCRUD
from Models.History import Historia, HistoriaCreate, HistoriaUpdate
from Models.User import User
from Utils.Services import current_user
from typing import List
import cloudinary.uploader
from pymongo.collection import Collection
from config.database import Database


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

@router.post("/api/historia/image/{historia_id}")
async def set_image(historia_id: str, file: UploadFile = File(...), user: User = Depends(current_user)):
    print(historia_id)
    try:
        # Asegurarse de que la historia exista
        collection: Collection = Database.get_connection().historias
        obj_id = ObjectId(historia_id)

        historia = collection.find_one({"_id": obj_id})

        if not historia:
            raise HTTPException(status_code=404, detail="Historia no encontrada")
            # raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Historia no encontrada")
        print(historia)
        # Leer el contenido del archivo
        file_content = await file.read()
        # Subir el archivo a Cloudinary
        upload_result = cloudinary.uploader.upload(file_content)

        image_url = upload_result['secure_url']

        # Actualizar la historia con la URL de la imagen
        collection.update_one({"_id": obj_id}, {"$set": {"imageURL": image_url}})
        
        # Actualizar la respuesta con la historia actualizada
        # historia["imageURL"] = image_url
        # return historia
        return image_url
    except Exception as e:
        print("Error",str(e))
        raise HTTPException(status_code=500, detail=f"Error al subir la imagen a Cloudinary: {str(e)}")
