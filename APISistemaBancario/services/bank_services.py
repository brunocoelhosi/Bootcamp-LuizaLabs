from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from exceptions import ClientAlreadyExistsError

from models.bank_models import ClientModel, AccountModel

from repository.bank_repository import create_client, get_by_cpf, create_account


AGENCIA = "0001"

clients = []
accounts = []

async def filtrar_cliente_por_cpf(cpf):
    result = await get_by_cpf(cpf)
    return result

async def create_new_client(client_schema):
    
    existing = await filtrar_cliente_por_cpf(client_schema.cpf)

    if existing:
        raise ClientAlreadyExistsError

    result = await create_client(client_schema)
    return result

async def create_new_account(client, account_schema):
    
    new_account = AccountModel(
        client = client,
        acc_id = len(accounts)+1,
        balance = account_schema.balance)

    result = await create_account(new_account)
    return result

async def deposit_account():
    pass