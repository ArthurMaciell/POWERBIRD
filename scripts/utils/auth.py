import os
from dotenv import load_dotenv

load_dotenv()


def get_rdstation_token():
    token = os.getenv("RDSTATION_TOKEN")
    if not token:
        raise ValueError("Token RD Station não encontrado. Verifique o arquivo .env")
    return token