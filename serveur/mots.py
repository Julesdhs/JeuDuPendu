from pydantic import BaseModel
from typing import List
from mot import Mot
from serveur.guess import Guess


class BDD(BaseModel):

    Liste: List[Mot] = []
    Listeguess: List[Guess] = []
