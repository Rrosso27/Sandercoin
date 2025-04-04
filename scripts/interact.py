import json
import os
from dotenv import load_dotenv
from web3 import Web3

# Cargar variables de entorno
load_dotenv()

INFURA_URL = os.getenv("INFURA_URL")
OWNER_ADDRESS = os.getenv("OWNER_ADDRESS")

# Conexión con Infura
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Cargar el ABI
ABI_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "artifacts", "contracts", "Sandercoin.sol", "Sandercoin.json"))
with open(ABI_PATH, "r") as file:
    contract_json = json.load(file)
    ABI = contract_json["abi"]

# Dirección del contrato desplegado (asegúrate de poner la correcta)
CONTRACT_ADDRESS = "0xTU_CONTRATO_EN_SEPOLIA"

# Conectarse al contrato
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

# Llamar una función de ejemplo (reemplaza según tu contrato)
total_supply = contract.functions.totalSupply().call()
print(f"Suministro total: {total_supply}")
