from pymongo import MongoClient

class Database:
    @staticmethod
    def get_connection():
        # Configura tu conexión a la base de datos MongoDB
        client = MongoClient("mongodb+srv://incedillo:U2vmSLzDmJNCT4aJ@cluster0.bm5ujfv.mongodb.net/?retryWrites=true&w=majority")
        return client.mydatabase  # Reemplaza "mydatabase" con el nombre de tu base de datos
