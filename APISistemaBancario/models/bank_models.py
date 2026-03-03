from pydantic import BaseModel
from pydantic import PositiveFloat

class ClientModel(BaseModel):
    nome: str 
    cpf : str
    adress: str 
    
class AccountModel(BaseModel):
    client: ClientModel
    acc_id: int
    balance: PositiveFloat