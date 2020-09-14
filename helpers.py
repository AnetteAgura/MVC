import exceptions
import pandas as pd

elemendid = []

# lisame ELEMENT juurde
def lisa_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus in nimetused:
        raise exceptions.ElementJubaOlemas("Element {} on juba olemas".format(nimetus))
    else:
        elemendid.append({"nimetus":nimetus, "hind":hind, "kogus":kogus})

# lisame ELEMENDID KORRAGA juurde
def lisa_elemendid(elementide_nimekiri):
    global elemendid
    elemendid = elementide_nimekiri

# loeme ELEMENDID korraga
def loe_elemendid():
    global elemendid
    loetud_elemendid = []
    for element in elemendid:
        loetud_elemendid.append(element)
    df = pd.DataFrame(loetud_elemendid)
    return df

# loeme KONKREETNE element
def loe_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
            nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        raise exceptions.ElementiEiOle("Elementi {} ei eksisteeri".format(nimetus))
    else:
       return elemendid[nimetused.index(nimetus)]

# uuendame KONKREETSET elementi
def uuenda_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        raise exceptions.ElementiEiSaa("Elementi {} ei saa uuendada, kuna ta ei eksisteeri".format(nimetus))
    else:
        elemendid[nimetused.index(nimetus)] = {"nimetus":nimetus, "hind":hind, "kogus":kogus}

# kustutame KONKREETSET elementi
def kustuta_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        print("Elementi {} ei saa kustutada, kuna ta ei eksisteeri".format(nimetus))
    else:
        elemendid.remove(elemendid[nimetused.index(nimetus)])

# kustutame KÕIK elemendid
def kustuta_elemendid():
    global elemendid
    elemendid.clear()

def main():
    # loome katseandmestik
    katse_elemendid = [
        {"nimetus": "leib", "hind":0.80, "kogus": 20},
        {"nimetus": "piim", "hind":0.50, "kogus": 15},
        {"nimetus": "vein", "hind":5.60, "kogus": 5},
    ]

    # testime elementide lisamist
    lisa_elemendid(katse_elemendid)

    # testime üksiku elemendi lisamist
    lisa_element("kohupiim", 0.90, 15)
    #lisa_element("vein", 5.60, 5)

    print(loe_elemendid())

    # testime elementide lugemist
    #print(loe_element("vein"))
    #print(loe_element("limonaad"))

    # testime elemendi uuendamist
    uuenda_element("vein", 10.0, 10)
    print(loe_element("vein"))

    # testime elemendi kustutamist
    kustuta_element("vein")
    print(loe_element("vein"))

    # testime elementide kustutamist
    kustuta_elemendid()
    print(loe_elemendid())

# käivitame
if __name__ == "__main__":
    main()