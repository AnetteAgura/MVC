import helpers


class Model:

    def __init__(self, elemendid):
        self.lisa_elemendid(elemendid)

    def lisa_elemendid(self, elemendid):
        helpers.lisa_elemendid(elemendid)

    def lisa_element(self, nimetus, hind, kogus):
        helpers.lisa_element(nimetus, hind, kogus)

    def loe_elemendid(self):
        return helpers.loe_elemendid()

    def loe_element(self, nimetus):
        return helpers.loe_element(nimetus)

    def uuenda_element(self, nimetus, hind, kogus):
        helpers.uuenda_element(nimetus, hind, kogus)

    def kustuta_element(self, nimetus):
        helpers.kustuta_element(nimetus)

    def kustuta_koik(self):
        helpers.kustuta_koik()