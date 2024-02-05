import asyncio
from bson import ObjectId
from fastapi import File, HTTPException, UploadFile
from pymongo.collection import Collection
from config.database import Database
from Models.History import Historia, HistoriaCreate, HistoriaUpdate
from typing import List
import cloudinary.uploader



class HistoriaCRUD:
    @staticmethod
    def create_historia(historia_create: HistoriaCreate,user_id:str) -> Historia:
        collection: Collection = Database.get_connection().historias
        historia_dict = historia_create.dict()
        historia_dict["user_id"] = user_id
        result = collection.insert_one(historia_dict)
        historia_dict['id'] = str(result.inserted_id)
        historia_dict['imageURL'] = ''
        
        return Historia(**historia_dict)

    @staticmethod
    def get_historia(historia_id: str) -> Historia:
        collection: Collection = Database.get_connection().historias
        historia_dict = collection.find_one({"_id": ObjectId(historia_id)})
        return Historia(**historia_dict)

    @staticmethod
    def update_historia(historia_id: str, historia_update: HistoriaUpdate) -> Historia:
        collection: Collection = Database.get_connection().historias
        updated_data = {k: v for k, v in historia_update.dict().items() if v is not None}
        collection.update_one({"_id": ObjectId(historia_id)}, {"$set": updated_data})
        return Historia(**updated_data, id=historia_id)

    @staticmethod
    def delete_historia(historia_id: str) -> None:
        collection: Collection = Database.get_connection().historias
        collection.delete_one({"_id": ObjectId(historia_id)})

    @staticmethod
    def get_all_historias(user_id: str) -> List[Historia]:
        collection: Collection = Database.get_connection().historias
        filter_criteria = {"user_id": user_id}
        
        # Asegurarse de que el campo 'imageURL' esté presente en cada documento
        historias_list = []
        for historia in collection.find(filter_criteria):
            historia_id = str(historia['_id'])
            fecha = historia.get('fecha')
            intensidad = historia.get('intensidad')
            blanco_biologico = historia.get('blanco_biologico')
            imageURL = historia.get('imageURL', None)  # Valor predeterminado si no existe el campo 'imageURL'
            
            historia_obj = Historia(id=historia_id, fecha=fecha, intensidad=intensidad, blanco_biologico=blanco_biologico, imageURL=imageURL)
            historias_list.append(historia_obj)
        return historias_list
    
    @staticmethod
    async def set_history_image(historia_id: str,file: UploadFile = File(...)):
        collection: Collection = Database.get_connection().historias
        obj_id = ObjectId(historia_id)

        historia = collection.find_one({"_id": obj_id})

        if not historia:
            raise HTTPException(status_code=404, detail="Historia no encontrada")

        # Leer el contenido del archivo como bytes
        file_content = await file.read()

        # Subir la imagen a Cloudinary
        upload_result = cloudinary.uploader.upload(file_content)
        image_url = upload_result['secure_url']

        # Actualizar la URL de la imagen en la historia
        collection.update_one({"_id": obj_id}, {"$set": {"imageURL": image_url}})

        # También puedes devolver la URL si es necesario
        return {"imageURL": image_url}
