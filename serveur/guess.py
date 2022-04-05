from pydantic import BaseModel
from mot import Mot

class Guess(BaseModel):
    mot: Mot
    erreurs: int
    letter: str
    