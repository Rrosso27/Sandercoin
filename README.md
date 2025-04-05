
  
  ##  Estructura Del Proyecto📝 
 
~~~bash  
 my-token-project/
│── artifacts/                   # Contratos generados 
│── ignition/                    #Almacena la configuración de los contratos inteligentes
│── contracts/                   # Carpeta para contratos Solidity
│   ├── MyToken.sol              # Código del contrato ERC-20
│── scripts/                     # Scripts Python para interactuar con el contrato
│   ├── deploy.py                # Script para desplegar el contrato
│   ├── interact.py              # Script para interactuar con el contrato
│── config/                      # Configuración del proyecto
│   ├── settings.py              # API Keys y configuración de red 
    ├── __init__.py              #El archivo __init__.py sirve para que Python reconozca la carpeta config/ como un módulo
│── requirements.txt             # Dependencias del proyecto
│── README.md                    # Explicación del proyecto
│── .env                         # Variables de entorno (clave privada, Infura API)
~~~

  
  ## Configurar las Variables de Entorno 🚀  
   Antes de ejecutar el programa, debes crear el archivo .env. En este archivo, deberás definir las siguientes variables de entorno.
  ~~~bash   
          PRIVATE_KEY="TU_CLAVE_PRIVADA"
          INFURA_URL="https://sepolia.infura.io/v3/TU_INFURA_API_KEY"
          OWNER_ADDRESS="TU_DIRECCIÓN"   
  ~~~

  
  ## Desplegar el Token 🔥  
  Ejecuta el siguiente comando para desplegar el contrato:
  ~~~bash   
  python scripts/deploy.py 
  ~~~
      
  ## Consultar el Balance🤔
  Después del despliegue, actualiza la dirección del contrato en interact.py y ejecuta:
   ~~~bash   
  python scripts/interact.py
  ~~~