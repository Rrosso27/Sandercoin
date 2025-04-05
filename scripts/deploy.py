import os
import json
from dotenv import load_dotenv
from web3 import Web3

# Cargar variables de entorno
load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
INFURA_URL = os.getenv("INFURA_URL")
OWNER_ADDRESS = os.getenv("OWNER_ADDRESS")

print("Private Key:", PRIVATE_KEY)
print("Infura URL:", INFURA_URL)
print("Owner Address:", OWNER_ADDRESS)

# Conexión a la red de Ethereum (por ejemplo Sepolia)
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Cargar ABI y bytecode del contrato compilado
with open("./artifacts/contracts/Sandercoin.sol/Sandercoin.json") as f:
    contract_data = json.load(f)
    abi = contract_data["abi"]
    bytecode = contract_data["bytecode"]

# Crear contrato
Sandercoin = w3.eth.contract(abi=abi, bytecode=bytecode)

# Definir el initialSupply (por ejemplo 1 millón de tokens con 18 decimales)
initial_supply = 1_000_000 * (10 ** 18)

# Preparar transacción
nonce = w3.eth.get_transaction_count(OWNER_ADDRESS)
transaction = Sandercoin.constructor(initial_supply).build_transaction({
    "chainId": 11155111,  # Sepolia
    "gasPrice": w3.eth.gas_price,
    "from": OWNER_ADDRESS,
    "nonce": nonce,
})

# Firmar y enviar transacción
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print("Transaction sent. Hash:", tx_hash.hex())

# Esperar confirmación
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Contract deployed at:", tx_receipt.contractAddress)

# Guardar dirección en archivo para usarlo luego
with open("contract_address.txt", "w") as f:
    f.write(tx_receipt.contractAddress)
