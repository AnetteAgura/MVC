from model import Model
from view import View
from controller import Controller

elemendid = [
    {"nimetus": "leib", "hind":0.80, "kogus": 20},
    {"nimetus": "piim", "hind":0.50, "kogus": 15},
    {"nimetus": "vein", "hind":5.60, "kogus": 5},
]
# testimine
# loome uus andmestik
pood = Controller(Model(elemendid), View())
# kõikide elementide kuvamine
pood.kuva_elemendid()
# konkreetse elemendi kuvamine
pood.kuva_element("piim")
# elemendi lisamine
pood.lisa_element("kohuke", 0.60, 15)
pood.lisa_element("kohuke", 0.60, 15)
pood.kuva_element("kohuke")
# elemendi uuendamine
pood.uuenda_element("vein", 10.0, 10)
# elemendi kustutamine
pood.kustuta_element("vein")