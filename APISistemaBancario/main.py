from fastapi import FastAPI, HTTPException, status
from services.bank_services import create_new_client, create_new_account, filtrar_cliente_por_cpf
from schemas.bank_schemas import ClientBaseSchema, AccountBaseSchema, AccountResponse
from typing import Union


from exceptions import ClientAlreadyExistsError
app = FastAPI()

@app.post("/transactions/deposit")
async def deposit():
    pass

@app.post("/transactions/withdraw")
async def withdraw():
    pass

@app.get("/account/transactions")
async def transactions():
    pass

@app.post("/client")
async def create_client(client: ClientBaseSchema):
    try:
        new_client = await create_new_client(client)
        return new_client
    except ClientAlreadyExistsError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Client already exists")

@app.post("/account", response_model=AccountResponse)
async def create_account(cpf: str, account: AccountBaseSchema):
    
    client = await filtrar_cliente_por_cpf(cpf)

    try:
        new_account = await create_new_account(client, account)
        return new_account
    except HTTPException:
        raise HTTPException





