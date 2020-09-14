import exceptions

class Controller:
    def __init__(self, mudel, vaade):
        self.mudel = mudel
        self.vaade = vaade

    # elementide kuvamine
    def kuva_elemendid(self):
        elemendid = self.mudel.loe_elemendid()
        self.vaade.kuva_elemendid(elemendid)

    # elemendi kuvamine
    def kuva_element(self, nimetus):
        element = self.mudel.loe_element(nimetus)
        self.vaade.kuva_element(nimetus, element)

    # elemendi lisamine
    def lisa_element(self, nimetus, hind, kogus):
        if(hind <= 0):
            print("Hind peab olema suurem kui 0 EUR")
        elif(kogus <= 0):
            print("Kogus peab olema suurem kui 0")
        try:
            self.mudel.lisa_element(nimetus, hind, kogus)
            self.vaade.lisa_element(nimetus, hind, kogus)
        except exceptions.ElementiEiOle as e:
            self.vaade.veateade_element_juba_olemas(nimetus, e)

    # elemendi uuendamine
    def uuenda_element(self, nimetus, hind, kogus):
        if (hind <= 0):
            print("Hind peab olema suurem kui 0 EUR")
        elif (kogus <= 0):
            print("Kogus peab olema suurem kui 0")
        else:
            vana_element = self.mudel.loe_element(nimetus)
            self.mudel.uuenda_element(nimetus, hind, kogus)
            self.vaade.uuenda_element(nimetus, vana_element['hind'], vana_element['kogus'], hind, kogus)

    # elemendi kustutamine
    def kustuta_element(self, nimetus):
        self.mudel.kustuta_element(nimetus)
        self.vaade.kustuta_element(nimetus)