from pymongo import MongoClient
import cloudinary
from config.environment import CLOUDINARY_API_KEY,CLOUDINARY_API_SECRET,CLOUDINARY_CLOUD_NAME,MONGO_URL

class Database:
    @staticmethod
    def get_connection():
        # Configura tu conexión a la base de datos MongoDB
        try:
            client = MongoClient("mongodb://root:example@localhost:27017/?tls=false")
            print(client.mydatabase)
            return client.mydatabase  # Reemplaza "mydatabase" con el nombre de tu base de datos
        except Exception as e:
            print(e)

    @staticmethod
    def configure_cloudinary():
        cloudinary.config(
            cloud_name=CLOUDINARY_CLOUD_NAME,
            api_key=CLOUDINARY_API_KEY,
            api_secret=CLOUDINARY_API_SECRET
        )
