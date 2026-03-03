from pydantic import BaseModel, PositiveFloat
from models.bank_models import ClientModel

class ClientBaseSchema(BaseModel):
    cpf: str
    nome: str
    adress: str
    
class AccountBaseSchema(BaseModel):
    balance: PositiveFloat
    
class AccountResponse(BaseModel):
    acc_id: int
    balance: PositiveFloat
    client: ClientModel

    class Config:
        from_attributes = True