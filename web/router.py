from fastapi import APIRouter, Request
from mot import Mot
from mots import BDD
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
