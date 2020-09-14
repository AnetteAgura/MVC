class View:
    def kuva_elemendid(self, elemendid):
        print("Kõik elemendid")
        for element in elemendid:
            print("- {}".format(element))

    def kuva_element(self, nimetus, element):
        print(" Kuvame {} elementi andmed".format(nimetus))
        print(element)

    def lisa_element(self, nimetus, hind, kogus):
        print("Elemendi lisamine")
        print("Lisatud {} hinnaga {}EUR koguses {}".format(nimetus, hind, kogus))

    def veateade_element_juba_olemas(self, nimetus, veateade):
        print("Elemendi {} juba olemas.".format(nimetus))
        print(veateade.args[0])

    def uuenda_element(self, nimetus, vana_hind, vana_kogus, uus_hind, uus_kogus):
        print("Elemendi {} uuendamine".format(nimetus))
        if(vana_hind != uus_hind):
            print("Muudetud hind: {} -> {}".format(vana_hind, uus_hind))
        if(vana_kogus != uus_kogus):
            print("Muudetud kogus: {} -> {}".format(vana_kogus, uus_kogus))

    def kustuta_element(self, nimetus):
        print("Elemendi {} kustutamine".format(nimetus))
        print("Element {} on kustutatud elementide nimekirjast".format(nimetus))
