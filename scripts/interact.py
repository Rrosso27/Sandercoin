from web3 import Web3
from config.settings import INFURA_URL, OWNER_ADDRESS

# Dirección del contrato desplegado (actualízala después del despliegue)
CONTRACT_ADDRESS = "0xTuContratoDesplegado"

# ABI del contrato (cópialo del deploy.py)
ABI = [...]  # Pegue el ABI generado aquí

# Conectar a Ethereum
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

# Consultar balance del dueño
balance = contract.functions.balanceOf(OWNER_ADDRESS).call()
print(f"Balance: {balance} MTK")
