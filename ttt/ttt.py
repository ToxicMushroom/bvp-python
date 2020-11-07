# Deze functie gaat na of alle elementen van een lijst gelijk zijn aan elkaar
# @param l  - de lijst waarvan de elementen nagekeken worden
#           - de functie mag ervan uitgaan dat l verwijst naar een geldige (lege of niet-lege) lijst
# @return   - True als alle elementen van l inderdaad gelijk zijn, anders False
#           - bemerk: de return-value van een lege lijst is True
def eentonige_lijst(l):
    eentonig = True  # variabele die bijhoudt of the lijst eentonig is
    if len(l) != 0:  # als de lijst leeg is False anders True
        vorigEl = l[0]  # aangezien we weten dat de lijst niet leeg is gaan we alle elementen vergelijken met het eerste element
        for el in l:  # voor elk element in de lijst
            if el != vorigEl:  # als het element niet gelijk is aan vorigEl
                eentonig = False  # de lijst is niet eentonig en eentonig wordt op False gezet
        return eentonig  # geef de waarde terug die in eentonig staat
    else:
        return True  # de lijst was leeg en dus eentonig dus True


# Deze functie gaat na of de 2-dimensionale data-structuur leeg is of niet
# @param m  - de 2-dimensionale data-structuur
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige (lege of niet-lege) 2-dim data-structuur
# @return   - True als m een lege lijst is (dus: [ ]), of slechts 1 element bevat dat op zich een lege lijst
#               is dus: [ [ ] ] );  anders False
def is_lege_matrix(m):
    if len(m) == 0:  # als de matrix leeg is
        return True
    elif len(m) == 1 and len(m[0]) == 0:  # als de matrix 1 lege rij bevat
        return True
    else:
        return False  # de matrix is hier niet leeg en bevat niet 1 lege rij


# Deze functie gaat na of de 2-dimensionale data-structuur een matrix is of niet
# @param m  - de 2-dimensionale data-structuur
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige (lege of niet-lege) 2-dim data-structuur, dit betekent dat als m niet leeg is, alle elementen van m een lijst zullen zijn
# @return   - True als alle 'rijen' van de data-structuur evenveel elementen bevatten, anders False
#           - bemerk: de return-value van een lege data-structuur is True
def is_matrix(m):
    if len(m) == 0:  # als de matrix leeg is
        return True

    columns = len(m[0])  # lengte van de eerste rij in de matrix wordt in de variabele columns gestoken
    for row in m:  # ga door elke rij in de matrix
        if len(row) != columns:  # check of de lengte van deze rij niet gelijk is aan de variabele columns
            return False  # De lengte was niet gelijk
        # deze rij had een gelijke lengte we gaan nu naar de volgende iteratie van de for loop
    return True  # alle rijen hadden dezelfde lengte als rij[0] en hebben dus allemaal dezelfde lengte en returnen we True


# Deze functie gaat na of alle elementen op de rand van een matrix gelijk zijn
# @param m  - de matrix
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige (lege of niet-lege) matrix, zoals
#             hierboven gedefinieerd
# @return   - True als alle elementen op de rand van m gelijk zijn, anders False
#           - bemerk: de return-value van een lege matrix is True
def gelijke_rand_matrix(m):
    # Note: hoeken worden 2 keer gechecked in deze implementatie maar er worden minder if statements per row uitgevoerd
    # resulteert in betere performantie voor grootte matrices en iets slechter voor kleiner matrices

    if len(m) == 0 or len(m[0]) == 0:  # kijk of de matrix een lege matrix is
        return True  # return true als dit het geval is
    rand_waarde = m[0][0]  # aangezien de matrix niet leeg is door de if statement hierboven kunnen we de eerste randwaarde veilig opslaan
    for el in m[0]:  # voor elk element in de eerste matrix rij (de eerste matrix rij bevat alleen maar randwaarden)
        if rand_waarde != el:  # als de randwaarde el verschilt van onze opgeslagen rand_waarde
            return False  # dan is de rand niet gelijk dus returnen we False
    for el in m[len(m) - 1]:  # voor elk element in de laatste matrix rij (de laatste matrix rij bevat alleen maar randwaarden)
        if rand_waarde != el:  # als de randwaarde el verschilt van onze opgeslagen rand_waarde
            return False  # dan is de rand niet gelijk dus returnen we False
    for row in m:  # voor elke rij in de matrix
        if rand_waarde != row[0] or rand_waarde != row[len(row) - 1]:  # als de rand_waarde verschilt van het eerste element in de rij of als de rand_waarde verschilt van het laatste element in de rij
            return False  # dan is de rand niet gelijk dus returnen we False

    return True  # Alle randwaarden waren gelijk aan onze randwaarde in m[0][0] en dus is de rand bestaande uit gelijke waarde en returnen we True


# Deze functie maakt een nieuwe matrix met alle elementen van een oorspronkelijke matrix zonder de rand
# @param m  - de oorspronkelijke matrix
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige, niet-lege matrix, zoals
#             hierboven gedefinieerd
# @return   - een matrix die alle elementen van m bevat zonder de rand-elementen
#           - bemerk: zie evt. de voorbeelden in de main-functie
def strip_matrix(m):
    nieuwe_matrix = []  # variabele nieuwe_matrix, deze wordt gevuld met de gestripte matrix
    y = 0  # variabele y om de y positie in de matrix in bij te houden
    for row in m:  # voor elke rij in de matrix
        if y != 0 and y != (len(m) - 1):  # als y verschilt van 0 en als y verschilt van de index van de positie van de laatste rij in de matrix
            nieuwe_matrix.append([])  # dan stoppen we een nieuwe rij in de nieuwe matrix
            x = 0  # variabele x om de x positie in de matrix in bij te houden
            for el in row:  # voor elk element el in de rij van de gegeven matrix
                if x != 0 and x != (len(row) - 1):  # als x verschilt van 0 en als x verschilt van de index van de positie van het laatste element in de rij
                    nieuwe_matrix[y-1].append(el)  # voeg het element el toe aan de laatste rij in de nieuwe matrix, y-1 zal altijd de laatste index zijn in de nieuwe matrix
                x += 1  # verhoog x met 1 zodat de index van het volgende element el in de iteratie door onze row de juiste x index heeft
        y += 1  # verhoog y met 1 zodat de index van de volgende row in de iteratie door onze matrix m de juiste y index heeft
    return nieuwe_matrix  # return de nieuwe matrix



def main():
    print("-- is_lege_matrix --")

    print(is_lege_matrix([]))  # True
    print(is_lege_matrix([[]]))  # True
    print(is_lege_matrix([[1, 1]]))  # False
    print(is_lege_matrix([[1, 2]]))  # False

    print("-- eentonige_lijst --")

    print(eentonige_lijst([]))  # True
    print(eentonige_lijst([1]))  # True
    print(eentonige_lijst([1, 1]))  # True
    print(eentonige_lijst([1, 2]))  # False
    print(eentonige_lijst([1, '1']))  # False

    print("-- is_matrix --")

    print(is_matrix([]))  # True
    print(is_matrix([[]]))  # True
    print(is_matrix([[1]]))  # True
    print(is_matrix([[1, 'a']]))  # True
    print(is_matrix([[1, 'a'], [True, 1.2]]))  # True
    print(is_matrix([[1, 'a'], [True, 1.2], ["hello"]]))  # False

    print("-- gelijke_rand_matrix --")

    print(gelijke_rand_matrix([[1, 'a'], [True, 1.2]]))  # False
    print(gelijke_rand_matrix([[1, 1, 1, 1],
                               [1, 1.2, True, 1],
                               [1, 1, 2, 1]]))  # False
    print(gelijke_rand_matrix([[1, 1, 1, 1],
                               [1, 1.2, True, 1],
                               [1, 1, 1, 1]]))  # True
    print(gelijke_rand_matrix([['a', 'a', 'a', 'a'],
                               ['a', 1.2, True, 'a'],
                               ['a', 1, 1, 'a'],
                               ['a', 'a', 'a', 'a']]))  # True
    print(gelijke_rand_matrix([['a', 'a', 'a', 'a'],
                               ['a', 1.2, True, 'a'],
                               ['a', 1, 1, 'a'],
                               ['a', 'b', 'a', 'a']]))  # False

    print("-- strip_matrix --")

    print(strip_matrix([['a', 'a', 'a', 'a'],
                        ['a', 1.2, True, 'a'],
                        ['a', 1, 1, 'a'],
                        ['a', 'b', 'a', 'a']]))  # [ [1.2, True], [1, 1] ]
    print(strip_matrix([['a', 'a', 'a', 'a'],
                        ['a', 1.2, True, 'a'],
                        ['a', 'b', 'a', 'a']]))  # [ [1.2, True] ]
    print(strip_matrix([[1, 1, 1, 1]]))  # een lege matrix, [ ] of [ [ ] ]


# VERANDER NIETS AAN DE LIJNEN HIERONDER, EN PLAATS ENKEL OPDRACHTEN BINNEN DE FUNCTIES HIERBOVEN
if __name__ == "__main__":
    main()
