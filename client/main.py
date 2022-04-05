from web_client import Requetes

choix = input("Voulez vous ajouter un mot (M) ou consulter la liste (L)? \n")
if choix == 'M':
    mot = input("Quel mot voulez vous ajouter ? \n")
    Requetes.ajouter_mot(mot)

Requetes.get_mots()
