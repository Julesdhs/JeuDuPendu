import requests


class Requetes:

    @staticmethod
    def ajouter_mot(mot):
        payload = {'caracteres': mot}
        requests.patch("http://localhost:8000/mot", json=payload)

    @staticmethod
    def get_mots():
        r = requests.get("http://localhost:8000/mots")
        print(r.json())
