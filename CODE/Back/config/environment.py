import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

ALGORITHM =  os.getenv('ALGORITHM')
"""
Algoritmo utilizado para codificar y decodificar el token JWT.

Valor:
    str: Valor de la variable de entorno 'ALGORITHM'.
"""

ACCESS_TOKEN_DURATION = int(os.getenv('ACCESS_TOKEN_DURATION'))
"""
Duración en minutos del token de acceso.

Valor:
    int: Valor entero de la variable de entorno 'ACCESS_TOKEN_DURATION'.
"""

SECRET = os.getenv('SECRET')
"""
Clave secreta utilizada para firmar el token JWT.

Valor:
    str: Valor de la variable de entorno 'SECRET'.
"""

CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET')
CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')
MONGO_URL = os.getenv('MONGO_URL')
