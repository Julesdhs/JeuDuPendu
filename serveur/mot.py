from pydantic import BaseModel

class Mot(BaseModel):
    id:int
    caracteres:str
