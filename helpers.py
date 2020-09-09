elemendid = []

# lisame ELEMENT juurde


def lisa_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        if nimetus in element.values():
            nimetused.append(nimetus)
    if nimetus in nimetused:
        print("Element {} on juba olemas.".format(nimetus))
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


def main():
    # loome katse andmestiku
    katse_elemendid = [
        {"nimetus": "leib", "hind": 0.80, "kogus": 20},
        {"nimetus": "piim", "hind": 0.50, "kogus": 15},
        {"nimetus": "vein", "hind": 5.60, "kogus": 5},
    ]

    # testime elemetide lisamist
    lisa_elemendid(katse_elemendid)
    print(elemendid)

    # lisame elemendi
    lisa_element("kohupiim", 0.90, 15)
    print(elemendid)

    lisa_element("leib", 0.80, 5)
    print(elemendid)

    # testime elemetide lugemist
    print(loe_elemendid())


# käivitamine
if __name__ == "__main__":
    main()