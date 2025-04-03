import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables desde .env

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
INFURA_URL = os.getenv("INFURA_URL")
OWNER_ADDRESS = os.getenv("OWNER_ADDRESS")

print("Private Key:", PRIVATE_KEY)
print("Infura URL:", INFURA_URL)
print("Owner Address:", OWNER_ADDRESS)
