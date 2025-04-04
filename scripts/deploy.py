import os
from dotenv import load_dotenv

load_dotenv()

INFURA_URL = os.getenv("INFURA_URL")
OWNER_ADDRESS = os.getenv("OWNER_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

print("Private Key:", PRIVATE_KEY)
print("Infura URL:", INFURA_URL)
print("Owner Address:", OWNER_ADDRESS)
