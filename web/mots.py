from pydantic import BaseModel
from typing import List
from mot import Mot


class BDD(BaseModel):

    Liste: List[Mot] = []
