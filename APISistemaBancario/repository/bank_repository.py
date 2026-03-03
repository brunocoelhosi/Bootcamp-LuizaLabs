from database.mongo import client_collection, account_collection

async def create_client(client_schema):
    result = await client_collection.insert_one(client_schema.model_dump())
    return {
        "id": str(result.inserted_id),
        **client_schema.model_dump()
    }

async def create_account(account_schema):
    result = await account_collection.insert_one(account_schema.model_dump())
    return {
        "id": str(result.inserted_id),
        **account_schema.model_dump()
    }
async def get_by_cpf(cpf):
    result = await client_collection.find_one({"cpf": cpf})
    return result   