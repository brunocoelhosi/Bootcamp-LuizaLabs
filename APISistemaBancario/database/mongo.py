from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://root:root@localhost:27017/"

client = AsyncIOMotorClient(MONGO_URL)

database = client.bank_db  # nome do banco
client_collection = database.clients
account_collection = database.accounts