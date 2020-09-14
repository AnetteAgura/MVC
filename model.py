import helpers


class Model:
    # konstruktor
    def __init__(self, elemendid):
        self.lisa_elemendid(elemendid)
    # elemendite lisamine
    def lisa_elemendid(self, elemendid):
        helpers.lisa_elemendid(elemendid)

    def lisa_element(self, nimetus, hind, kogus):
        helpers.lisa_element(nimetus, hind, kogus)
    # elementide lugemine
    def loe_elemendid(self):
        return helpers.loe_elemendid()

    def loe_element(self, nimetus):
        return helpers.loe_element(nimetus)
    # elemendi uuendamine
    def uuenda_element(self, nimetus, hind, kogus):
        helpers.uuenda_element(nimetus, hind, kogus)
    # elementide kustutamine
    def kustuta_element(self, nimetus):
        helpers.kustuta_element(nimetus)

    def kustuta_elemendid(self):
        helpers.kustuta_elemendid()