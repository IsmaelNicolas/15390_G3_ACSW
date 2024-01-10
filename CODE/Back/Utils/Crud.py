from bson import ObjectId
from pymongo.collection import Collection
from config.database import Database
from Models.History import Historia, HistoriaCreate, HistoriaUpdate

class HistoriaCRUD:
    @staticmethod
    def create_historia(historia_create: HistoriaCreate) -> Historia:
        collection: Collection = Database.get_connection().historias
        historia_dict = historia_create.dict()
        result = collection.insert_one(historia_dict)
        historia_dict['_id'] = str(result.inserted_id)
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
