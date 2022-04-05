from fastapi import APIRouter, Request
from mot import Mot
from mots import BDD
from guess import Guess
import random

router = APIRouter()

BaseDeMots = BDD()


@router.get("/mots", tags=["avoir la liste de mots"])
def ListerMots():
    return BaseDeMots.Liste


@router.patch("/mot", tags=["ajouter un mot"])
async def AjouteMot(request: Request):
    json = await request.json()
    mot = json['caracteres']
    Obj = Mot(len(BaseDeMots.Liste), caracteres=mot)
    BaseDeMots.Liste.append(Obj)


@router.get("/init", tags=["démarrer une partie"])
def Demarrer():
    idmot = random.randint(0, len(BaseDeMots.Liste))
    mot = BaseDeMots.Liste[idmot]
    return len(mot)*'-'

@router.patch("/guess", tags=["faire un guess"])
async def AjouteMot(request: Request):
    json = await request.json()
    mot = json['caracteres']
    Obj = Mot(len(BaseDeMots.Liste), caracteres=mot)
    BaseDeMots.Liste.append(Obj)