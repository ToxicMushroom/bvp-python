#########################################################################
# Enkele functies voor het aanmaken en invullen van de datastructuur
#########################################################################

# in mijn implementatie is een netwerk een dictionary met als keys de bedrijven en als values de leveringen dictionary
# de leveringen dictionary heeft als keys de bedrijven waaraan geleverd wordt en als keys de snelheid

def creeer_leeg_netwerk():
    # deze functie creeert een lege data-structuur, d.w.z. een initiële
    # data-structuur, zonder gegevens over bedrijven en afhankelijkheden
    # en geeft die data-structuur als return-waarde terug
    return {}  # leeg netwerk


def voeg_bedrijf_toe(sc, naam_bedrijf):
    # deze functie voegt aan de data-structuur ‘sc' (afkorting van ‘supply chain)
    # de informatie toe over het bedrijf naam_bedrijf; deze functie geeft als return-
    # waarde de aangepaste datastructuur terug; als een bedrijf met dezelfde naam eerder
    # al werd toegevoegd, dan verandert er niets aan sc
    if not is_bedrijf(sc, naam_bedrijf):  # kijkt of het bedrijf al niet in het netwerk zit
        sc[naam_bedrijf] = {}  # voeg het bedrijf toe aan het netwerk met een lege dictionary als leveringen
    return sc  # return het aangepaste netwerk


def voeg_afhankelijkheid_toe(sc, naam_bedrijf1, naam_bedrijf2, snelheid):
    # als beide bedrijven al in het netwerk werden toegevoegd, dan voegt deze functie
    # aan de datastructuur toe dat bedrijf1 goederen levert aan bedrijf2 en aan welke
    # snelheid; als één of beide bedrijven niet in het netwerk voorkomen, dan verandert de
    # datastructuur gewoonweg niet; als de afhankelijkheid al bestond (eventueel met
    # een andere snelheid), mag deze geen 2de maal worden toegevoegd;
    # deze functie geeft als return-waarde de (eventueel aangepaste) datastructuur terug
    if is_bedrijf(sc, naam_bedrijf1) and is_bedrijf(sc, naam_bedrijf2):  # check of beide bedrijven bestaan
        leveringen = sc[naam_bedrijf1]  # slaag de leveringen van bedrijf1 op in een variabele
        if naam_bedrijf2 not in leveringen:  # check of bedrijf2 nog niet aanwezig is in de leveringen van bedrijf1
            leveringen[
                naam_bedrijf2] = snelheid  # we kennen de snelheid waarmee bedrijf 1 aan bedrijf 2 levert toe aan de leveringen
            sc[naam_bedrijf1] = leveringen  # we kennen de leveringen toe aan het bedrijf in het netwerk
    return sc  # return het aangepaste netwerk


#########################################################################
# Twee functies voor eenvoudige vragen aan de datastructuur
#########################################################################

def is_bedrijf(sc, naam_bedrijf):
    # deze functie geeft een boolean als return-waarde die aangeeft of het bedrijf
    # met deze naam al in het netwerk ‘sc’ was toegevoegd
    return naam_bedrijf in sc  # return of het bedrijf in het netwerk zit


def levert_aan(sc, naam_bedrijf1, naam_bedrijf2):
    # deze functie geeft als return-waarde de snelheid aan welke bedrijf1 rechtstreeks
    # goederen levert aan bedrijf2: indien één of beide bedrijven niet in het netwerk
    # zijn opgenomen of indien ze geen afhankelijkheid hebben, geeft de functie
    # uiteraard 0 als resultaat
    if is_bedrijf(sc, naam_bedrijf1):  # kijk of bedrijf1 in het netwerk zit
        leveringen = sc[naam_bedrijf1]  # slaag de leveringen van bedrijf1 op in een variabele
        if naam_bedrijf2 in leveringen:  # kijk of bedrijf2 in de leveringen zit
            return leveringen[naam_bedrijf2]  # return de snelheid van het leveren aan bedrijf2

    return 0  # snelheid 0 wanneer niet voldaan aan de 2 if condities


#########################################################################
# Enkele meer geavanceerde functies die de datastructuur ondervragen
#########################################################################

def uitstroomsnelheid_goederen(sc, naam_bedrijf):
    # deze functie geeft de totale snelheid van output van producten door een bepaald
    # bedrijf als return-waarde op basis van de som van de snelheden van alle relevante
    # afhankelijkheden; indien het bedrijf niet bestaat geeft de functie 0 als resultaat
    totaal = 0  # variabele om de totale uitstroomsnelheid in te bewaren
    if not is_bedrijf(sc, naam_bedrijf):  # check of het bedrijf niet bestaan in het netwerk
        return totaal  # return totaal (0 in dit geval) wanneer het bedrijf niet bestaat

    leveringen = sc[naam_bedrijf]  # slaag de leveringen van het bedrijf op in een variabele
    for naam_bedrijf2 in leveringen:  # we itereren door elk bedrijf in de leveringen
        snelheid = leveringen[naam_bedrijf2]  # haal de snelheid waaaraan bedrijf levert aan bedrijf2 uit de leveringen
        totaal += snelheid  # tel de snelheid op bij het totaal

    return totaal  # return de total uitvoersnelheid


def alfabetisch_x_voor_y(x, y):  # x en y zijn strings, deze functie returned of x voor y moet geplaatst worden (
    # alfabetisch of kortst)
    kleinst = min(len(x), len(y))  # de lengte van de korste string wordt opgeslagen in kleinst
    for i in range(kleinst):  # voor alle getallen van 0 tot kleinst [0; kleinst[
        letter_x = x[i]  # karakter i in de string x wordt toegekent aan letter_x
        letter_y = y[i]  # karakter i in de string y wordt toegekent aan letter_y
        if letter_x < letter_y:  # kijk of letter x een kleinere waarde heeft dan letter y
            return True  # return true, x is alfabetisch voor y
        elif letter_x > letter_y:  # kijk of letter x een grotere waarde heeft dan letter y
            return False  # return false, x is niet alfabetisch voor y
        # letter x en y zijn gelijk (zelfde karakter), er wordt nu naar de volgende letter gekeken in de volgende
        # iteratie of de lengte wordt vergeleken

    # indien we hier komen dan begint 1 van de 2 strings met de andere string
    if len(x) < len(y):  # kijk of de lengte van string x kleiner is dan de lengte van string y
        return True  # korter komt alfabetisch eerst
    else:
        return False  # wanneer gelijk of niet alfabetisch eerst


def grootste_leveraars(sc):
    # deze functie geeft de lijst van de namen van bedrijven als return-waarde
    # die gesorteerd is van groot naar klein op basis van de uitstroomsnelheid; bedrijven met dezelfde
    # uitstroomsnelheid worden alfabetisch gesorteerd
    lijst = []  # lijst die uiteindelijk de gesorteerde bedrijven zal bevatten

    # Alternatieve beter sort
    gesorteerd = sorted(sc.items(), key=lambda x: (-uitstroomsnelheid_goederen(sc, x[0]), x[0]))
    for pair in gesorteerd:
        lijst.append(pair[0])

    return lijst

    # Vreemde custom sorter toen mijn hersenen niet werkte
    bedrijf_uitstroomsnelheid_tupples = []  # hierin worden alle bedrijven en hun uitstroomsnelheid in tuples bewaard
    for naam_bedrijf in sc:  # we itereren over elk bedrijf in het netwerk

        # het tupple van het de bedrijfsnaam en zijn uitstroomsnelheid wordt toegevoegd aan bedrijf_uitstroomsnelheid_tupples
        bedrijf_uitstroomsnelheid_tupples.append((naam_bedrijf, uitstroomsnelheid_goederen(sc, naam_bedrijf)))

    bedrijf_uitstroomsnelheid_sorted_tuples = []  # hierin worden alle bedrijven en hun uitstroomsnelheid in tuples bewaard maar nu in gestorteerde volgorde zoals gespecifieerd in de opgave bovenaan
    for bedrijf_tupple in bedrijf_uitstroomsnelheid_tupples:  # itereren over elk tuple in bedrijf_uitstroomsnelheid_tupples
        if len(
                bedrijf_uitstroomsnelheid_sorted_tuples) == 0:  # indien dit de eerste iteratie is (elke iteratie wordt er een element toegevoegd aan de gesorteerde versie van de array) dan appenden we gewoon dit tupple
            bedrijf_uitstroomsnelheid_sorted_tuples.append(bedrijf_tupple)  # append eerste tupple
        else:  # niet eerste iteratie
            counter = 0  # counter variabele die de index in de iteratie over bedrijf_uitstroomsnelheid_sorted_tuples bijhoudt
            added = False  # variabele om tussen 2 statussen te kunnen switchen zonder breaks :)
            for sorted_bedrijf_tupple in bedrijf_uitstroomsnelheid_sorted_tuples:  # itereren over de al gesorteerde tuples
                if not added:  # kijk of het bedrijf_tupple nog niet is toegevoegd aan de gesorteerde tupples
                    if sorted_bedrijf_tupple[1] < bedrijf_tupple[
                        1]:  # kijk of de uitvoersnelheid van het gesorteerde tupple kleiner is dan de uitvoersnelheid van bedrijf_tupple
                        bedrijf_uitstroomsnelheid_sorted_tuples.insert(counter,
                                                                       bedrijf_tupple)  # uitvoersnelheid was kleiner dus bedrijf_tupple wordt voor sorted_bedrijf_tupple geinsert
                        added = True  # verrander added naar true zodat het niet in de volgende iteraties geinsert wordt
                    elif (sorted_bedrijf_tupple[1] == bedrijf_tupple[1]) and \
                            alfabetisch_x_voor_y(bedrijf_tupple[0], sorted_bedrijf_tupple[
                                0]):  # anders kijken we of (de uitvoersnelheid gelijk is en dat bedrijf_naam van bedrijf_tupple alfabetisch voor bedrijf_naam van sorted_bedrijf_tupple komt)
                        bedrijf_uitstroomsnelheid_sorted_tuples.insert(counter,
                                                                       bedrijf_tupple)  # bedrijf_tuple komt alfabetisch voor sorted_bedrijf_tupple en wordt hier geinsert
                        added = True  # verrander added naar true zodat het niet in de volgende iteraties geinsert wordt
                    counter += 1  # verhoog de counter met 1 zodat de index voor insertion meegaat met het element van de volgende iteratie

            if not added:  # als wanneer door de bedrijf_uitstroomsnelheid_sorted_tuples te itereren geen plek is gevonden waar het tuple voor het element moest van de iteratie dan zal het achteraan de array thuishoren
                bedrijf_uitstroomsnelheid_sorted_tuples.append(
                    bedrijf_tupple)  # append het bedrijf_tuppel aan bedrijf_uitstroomsnelheid_sorted_tuples

    # de bedrijf_uitstroomsnelheid_sorted_tuples werd voledig gesorteerd opgebouwd maar het zijn nog tuples dus moeten we het nog omzetten:
    for bedrijf_tuple in bedrijf_uitstroomsnelheid_sorted_tuples:  # we itereren over elk tuple in de variabele bedrijf_uitstroomsnelheid_sorted_tuples
        lijst.append(
            bedrijf_tuple[0])  # het bedrijf wordt uit het tuple gehaald en op de gesorteerde lijst variabele geappend

    return lijst  # geef de lijst terug


def instroomsnelheid_goederen(sc, naam_bedrijf):
    # deze functie geeft de totale snelheid van input van producten voor een bepaald
    # bedrijf als return-waarde op basis van alle relevante afhankelijkheden; indien
    # het bedrijf niet bestaat geeft de functie 0 als resultaat
    if not is_bedrijf(sc, naam_bedrijf):  # check of het bedrijf niet bestaat in het netwerk
        return 0  # wanneer het bedrijf niet bestaat is de instroomsnelheid 0 en returnen we 0

    totaal = 0  # variabele om de totale instroomsnelheid in bij te houden
    for naam_bedrijf2 in sc:  # we itereren over elk bedrijf in het netwerk
        totaal += levert_aan(sc, naam_bedrijf2,
                             naam_bedrijf)  # de lever_aan snelheid van bedrijf_2 aan bedrijf_1 wordt opgetelt bij het totaal

    return totaal  # return het totaal


def levert_indirect_aan(sc, naam_bedrijf1, naam_bedrijf2):
    # deze functie geeft een boolean als return-waarde die ‘true’ teruggeeft als bedrijf1
    # rechtstreeks of onrechtstreeks (via een aantal andere bedrijven) goederen levert aan
    # bedrijf2; dus bv. als bedrijf1 levert aan bedrijf3, dat levert aan bedrijf 4, dat op
    # zijn beurt levert aan bedrijf2, dan levert bedrijf1 indirect aan bedrijf2
    if not is_bedrijf(sc, naam_bedrijf1) or not is_bedrijf(sc,
                                                           naam_bedrijf2):  # kijk of 1 van de 2 bedrijven niet bestaat
        return False  # als 1 niet bestaat dan kunnen ze niet inderect aan elkaar leveren

    results = []  # array die alle recursieve resutaten bijhoudt
    found = False  # boolean die de staat in de for loop switched zodat veel recursie vermeden wordt wanneer een match is gevonden

    leveringen = sc[naam_bedrijf1]  # leveringen van bedrijf1 in het netwerk
    for sub_bedrijf in leveringen:  # itereren over alle bedrijven waaraan bedrijf1 aan levert
        if sub_bedrijf == naam_bedrijf2:  # check of sub_bedrijf gelijk is aan bedrijf2 en bedrijf1 dus direct levert aan bedrijf2
            results.append(True)  # append True aan de resultaten aangezien een match is gevonden
            found = True  # variabele die verdere recursie vermijdt wanneer True wordt op true gezet
        elif not found:  # check of nog niet gevonden
            results.append(levert_indirect_aan(sc, sub_bedrijf,
                                               naam_bedrijf2))  # voeg het resultaat van de recursie toe aan de resultaten
    return any(results)  # als 1 van de results True zijn returned de functie true


#############################################################################
# Hieronder vind je 1 voorbeeld van een hoofdprogramma. Dit pas je uiteraard
# aan om je programma te testen, en wordt op zich niet verbeterd.
# Van dit voorbeeldje zie je hieronder ook een schematische voorstelling.
#############################################################################

def main():
    print("-- bedrijven toevoegen --")

    sc = creeer_leeg_netwerk()
    print(is_bedrijf(sc, 'Bedrijf_A'))  # False
    print(is_bedrijf(sc, 'Bedrijf_B'))  # False
    sc = voeg_bedrijf_toe(sc, 'Bedrijf_A')
    print(is_bedrijf(sc, 'Bedrijf_A'))  # True
    print(is_bedrijf(sc, 'Bedrijf_B'))  # False
    sc = voeg_bedrijf_toe(sc, 'Bedrijf_B')
    print(is_bedrijf(sc, 'Bedrijf_B'))  # True
    sc = voeg_bedrijf_toe(sc, 'Bedrijf_A')
    print(is_bedrijf(sc, 'Bedrijf_A'))  # True

    print("-- leveringen toevoegen --")

    sc = voeg_bedrijf_toe(sc, 'Bedrijf_C')
    sc = voeg_bedrijf_toe(sc, 'Bedrijf_D')
    sc = voeg_bedrijf_toe(sc, 'Bedrijf_E')
    sc = voeg_afhankelijkheid_toe(sc, 'Bedrijf_A', 'Bedrijf_B', 5)
    sc = voeg_afhankelijkheid_toe(sc, 'Bedrijf_A', 'Bedrijf_C', 7)
    sc = voeg_afhankelijkheid_toe(sc, 'Bedrijf_B', 'Bedrijf_D', 4)
    print(levert_aan(sc, 'Bedrijf_B', 'Bedrijf_D'))  # 4
    print(levert_aan(sc, 'Bedrijf_B', 'Bedrijf_E'))  # 0
    print(levert_aan(sc, 'Bedrijf_D', 'Bedrijf_B'))  # 0
    sc = voeg_afhankelijkheid_toe(sc, 'Bedrijf_B', 'Bedrijf_E', 8)
    sc = voeg_afhankelijkheid_toe(sc, 'Bedrijf_E', 'Bedrijf_C', 9)
    print(levert_aan(sc, 'Bedrijf_A', 'Bedrijf_B'))  # 5
    print(levert_aan(sc, 'Bedrijf_B', 'Bedrijf_E'))  # 8
    print(levert_aan(sc, 'Bedrijf_C', 'Bedrijf_E'))  # 0
    print(levert_aan(sc, 'Bedrijf_F', 'Bedrijf_A'))  # 0
    print(levert_aan(sc, 'Bedrijf_A', 'Bedrijf_F'))  # 0

    print("-- uitstroomsnelheid goederen --")

    print(uitstroomsnelheid_goederen(sc, 'Bedrijf_A'))  # 12
    print(uitstroomsnelheid_goederen(sc, 'Bedrijf_E'))  # 9
    print(uitstroomsnelheid_goederen(sc, 'Bedrijf_C'))  # 0
    print(uitstroomsnelheid_goederen(sc, 'Bedrijf_F'))  # 0

    print("-- grootste leveraars --")

    print(grootste_leveraars(sc))  # ['Bedrijf_A', 'Bedrijf_B', 'Bedrijf_E', 'Bedrijf_C', 'Bedrijf_D',]

    print("-- instroomsnelheid goederen --")
    print(instroomsnelheid_goederen(sc, 'Bedrijf_A'))  # 0
    print(instroomsnelheid_goederen(sc, 'Bedrijf_E'))  # 8
    print(instroomsnelheid_goederen(sc, 'Bedrijf_C'))  # 16
    print(instroomsnelheid_goederen(sc, 'Bedrijf_F'))  # 0

    print("-- indirecte leveringen --")
    print(levert_indirect_aan(sc, 'Bedrijf_A', 'Bedrijf_B'))  # True
    print(levert_indirect_aan(sc, 'Bedrijf_B', 'Bedrijf_C'))  # True
    print(levert_indirect_aan(sc, 'Bedrijf_C', 'Bedrijf_B'))  # False
    print(levert_indirect_aan(sc, 'Bedrijf_A', 'Bedrijf_F'))  # False
    print(levert_indirect_aan(sc, 'Bedrijf_F', 'Bedrijf_A'))  # False
    print(levert_indirect_aan(sc, 'Bedrijf_A', 'Bedrijf_D'))  # True
    print(levert_indirect_aan(sc, 'Bedrijf_C', 'Bedrijf_E'))  # False


# VERANDER NIETS AAN DE LIJNEN HIERONDER, EN PLAATS ENKEL OPDRACHTEN BINNEN DE FUNCTIES HIERBOVEN
if __name__ == "__main__":
    main()
