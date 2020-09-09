elemendid = []

# lisame ELEMENT juurde


def lisa_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus in nimetused:
        return "Element {} on juba olemas.".format(nimetus)
    else:
        elemendid.append({"nimetus": nimetus, "hind": hind, "kogus": kogus})


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
    return loetud_elemendid


# loeme konkreetne element

def loe_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
            nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        return "Elementi {} ei eksisteeri.".format(nimetus)
    else:
        return elemendid[nimetused.index(nimetus)]


# uuendame KONKREETSE elemendi

def uuenda_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        print("Elementi {} ei saa uuendada, kuna see ei eksisteeri.".format(nimetus))
    else:
        elemendid[nimetused.index(nimetus)] = {"nimetus": nimetus, "hind": hind, "kogus": kogus}


# kustutame KONKREETSE elemendi

def kustuta_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        print("Elementi {} ei saa kustutada, kuna see ei eksisteeri.".format(nimetus))
    else:
        elemendid.remove(elemendid[nimetused.index(nimetus)])


# kustutame TERVE listi

def kustuta_koik():
    global elemendid
    elemendid.clear()


def main():
    # loome katse andmestiku
    katse_elemendid = [
        {"nimetus": "leib", "hind": 0.80, "kogus": 20},
        {"nimetus": "piim", "hind": 0.50, "kogus": 15},
        {"nimetus": "vein", "hind": 5.60, "kogus": 5},
    ]

    # testime elemetide lisamist
    lisa_elemendid(katse_elemendid)

    # lisame elemendi
    lisa_element("kohupiim", 0.90, 15)

    lisa_element("leib", 0.80, 5)

    # testime elemetide lugemist
    # print(loe_element("vein"))

    # testime elemedi uuendamist
    uuenda_element("limonaad", 10.0, 10)

    # testime elemendi kustutamist
    kustuta_element("vein")
    print(loe_element("vein"))

    # testime kõikide elementide kustutamist
    kustuta_koik()
    print(loe_elemendid())


# käivitamine
if __name__ == "__main__":
    main()