import importlib


def print_result(test_nb, succes_boolean):
    test_string = 'Test ' + str(test_nb)+':'
    if succes_boolean:
        print(test_string, 'correct')
    else:
        print(test_string, 'foutief')

# programma blijkt werken bij duplicate bedrijven
# line 14 bvp_practicum2_empty.py
def custom_test_bedrijf_duplicaat(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        succes = bvp.is_bedrijf(netwerk, "Farm A") is True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)


# als hetzelfde bedrijf twee keer wordt toegevoegd, mag er niks veranderen
# aan de structuur
# line 14 bvp_practicum2_empty.py
def custom_test_bedrijf_duplicaat_geen_verandering(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Farm B", 10)
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        snelheid = bvp.levert_aan(netwerk, "Farm A", "Farm B")
        succes = snelheid == 10
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)

# als er geen afhankelijkheid is tussen de bedrijven zal de snelheid 0 zijn
# line 41 bvp_practicum2_empty.py
def custom_test_geen_afhankelijkheid(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        snelheid = bvp.levert_aan(netwerk, "Farm A", "Farm B")
        succes = snelheid == 0
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)


# als de afhankelijkheid (en snelheid) al bestaat, mag die niet veranderen
# line 23 bvp_practicum2_empty.py
def custom_test_afhankelijkheid_duplicaat(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Farm B", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Farm B", 20)
        snelheid = bvp.levert_aan(netwerk, "Farm A", "Farm B")
        succes = snelheid == 10
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)

# afhankelijkheid tussen bedrijf 1 en bedrijf2 betekent NIET dat bedrijf2 aan
# bedrijf1 levert
def custom_test_afhankelijkheid_juiste_volgorde(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Farm B", 10)
        snelheid1 = bvp.levert_aan(netwerk, "Farm A", "Farm B")
        snelheid2 = bvp.levert_aan(netwerk, "Farm B", "Farm A")
        succes = snelheid1 == 10 and snelheid2 == 0
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)


# als een of beide bedrijven niet in het netwerk voorkomen, dan verandert de
# datastructuur gewoonweg niet
# https://p.cygnus.cc.kuleuven.be/webapps/discussionboard/do/message?action=list_messages&course_id=_946261_1&nav=discussion_board_entry&conf_id=_1664100_1&forum_id=_940270_1&message_id=_7293324_1
# line 21 bvp_practicum2_empty.py
def custom_test_afhankelijkheid_onbestaande_bedrijven(bvp):
    # Test 1 (beide bedrijven bestaat niet)
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Farm B", 10)
        snelheid = bvp.levert_aan(netwerk, "Farm A", "Farm B")
        succes = snelheid == 0
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)

    # Test 2 (bedrijf1 bestaat niet)
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Farm B", 10)
        snelheid = bvp.levert_aan(netwerk, "Farm A", "Farm B")
        succes = snelheid == 0
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)

    # Test 3 (bedrijf2 bestaat niet)
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Farm B", 10)
        snelheid = bvp.levert_aan(netwerk, "Farm A", "Farm B")
        succes = snelheid == 0
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)


# indien het bedrijf niet bestaat geeft de functie 0 als resultaat
# line 53 bvp_practicum2_empty.py
def custom_test_uitstroomsnelheid_onbestaand_bedrijf(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Farm B", 10)
        uitstroomsnelheid = bvp.uitstroomsnelheid_goederen(netwerk, "Farm C")
        succes = uitstroomsnelheid == 0
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)


# indien het bedrijf niet bestaat geeft de functie 0 als resultaat
# line 65 bvp_practicum2_empty.py
def custom_test_instroomsnelheid_onbestaand_bedrijf(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Farm B", 10)
        uitstroomsnelheid = bvp.instroomsnelheid_goederen(netwerk, "Farm C")
        succes = uitstroomsnelheid == 0
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)


def test_bedrijf_toevoegen(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Foundry")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery W")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery M")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Manufacturer")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Detailer")
        succes = bvp.is_bedrijf(netwerk, "Refinery W") is True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)

    # Test 2
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Foundry")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery W")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery M")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Manufacturer")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Detailer")
        succes = bvp.is_bedrijf(netwerk, "Refinery X") is False
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)


def test_afhankelijkheid_toevoegen(bvp):
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Foundry")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery W")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery M")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Manufacturer")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Detailer")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Refinery A", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm B", "Refinery B", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine A", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine B", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery A", "Refinery W", 8)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Manufacturer", 1)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Foundry", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery W", "Manufacturer", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery M", "Manufacturer", 6)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Manufacturer", "Detailer", 10)
        succes = bvp.levert_aan(netwerk, "Farm A", "Refinery A") == 10
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)


def test_uitstroomsnelheid(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Foundry")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery W")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery M")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Manufacturer")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Detailer")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Refinery A", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm B", "Refinery B", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine A", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine B", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery A", "Refinery W", 8)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Manufacturer", 1)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Foundry", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery W", "Manufacturer", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery M", "Manufacturer", 6)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Manufacturer", "Detailer", 10)
        succes = bvp.uitstroomsnelheid_goederen(netwerk, "Farm A") == 10
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)

    # Test 2
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Foundry")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery W")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery M")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Manufacturer")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Detailer")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Refinery A", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm B", "Refinery B", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine A", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine B", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery A", "Refinery W", 8)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Manufacturer", 1)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Foundry", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery W", "Manufacturer", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery M", "Manufacturer", 6)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Manufacturer", "Detailer", 10)
        succes = bvp.uitstroomsnelheid_goederen(netwerk, "Refinery B") == 6
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)


def test_grootste_leveraars(bvp):
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Foundry")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery W")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery M")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Manufacturer")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Detailer")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Refinery A", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm B", "Refinery B", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine A", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine B", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery A", "Refinery W", 8)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Manufacturer", 1)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Foundry", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery W", "Manufacturer", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery M", "Manufacturer", 6)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Manufacturer", "Detailer", 10)
        lijst = bvp.grootste_leveraars(netwerk)
        # ['Farm A', 'Farm B', 'Manufacturer', 'Refinery A', 'Refinery B', 'Refinery M', 'Foundry', 'Mine A', 'Mine B',
        # 'Refinery W', 'Detailer']
        succes = lijst[0] == "Farm A" and lijst[1] == "Farm B" and lijst[2] == "Manufacturer" and lijst[3] == \
                 "Refinery A" and lijst[4] == "Refinery B" and lijst[5] == "Refinery M" and lijst[6] == "Foundry" and \
                 lijst[7] == "Mine A" and lijst[8] == "Mine B" and lijst[9] == "Refinery W" and lijst[10] == "Detailer"
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)


def test_instroomsnelheid(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Foundry")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery W")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery M")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Manufacturer")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Detailer")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Refinery A", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm B", "Refinery B", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine A", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine B", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery A", "Refinery W", 8)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Manufacturer", 1)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Foundry", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery W", "Manufacturer", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery M", "Manufacturer", 6)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Manufacturer", "Detailer", 10)
        succes = bvp.instroomsnelheid_goederen(netwerk, "Refinery A") == 10
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)

    # Test 2
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Foundry")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery W")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery M")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Manufacturer")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Detailer")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Refinery A", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm B", "Refinery B", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine A", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine B", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery A", "Refinery W", 8)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Manufacturer", 1)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Foundry", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery W", "Manufacturer", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery M", "Manufacturer", 6)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Manufacturer", "Detailer", 10)
        succes = bvp.instroomsnelheid_goederen(netwerk, "Manufacturer") == 12
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)


def test_levert_indirect_aan(bvp):
    # Test 1
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Foundry")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery W")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery M")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Manufacturer")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Detailer")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Refinery A", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm B", "Refinery B", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine A", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine B", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery A", "Refinery W", 8)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Manufacturer", 1)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Foundry", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery W", "Manufacturer", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery M", "Manufacturer", 6)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Manufacturer", "Detailer", 10)
        succes = bvp.levert_indirect_aan(netwerk, "Farm A", "Refinery A") is True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)

    # Test 2
    succes = False
    try:
        netwerk = bvp.creeer_leeg_netwerk()
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Farm B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Mine B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery A")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery B")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Foundry")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery W")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Refinery M")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Manufacturer")
        netwerk = bvp.voeg_bedrijf_toe(netwerk, "Detailer")
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm A", "Refinery A", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Farm B", "Refinery B", 10)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine A", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Mine B", "Foundry", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery A", "Refinery W", 8)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Manufacturer", 1)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery B", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Foundry", "Refinery M", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery W", "Manufacturer", 5)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Refinery M", "Manufacturer", 6)
        netwerk = bvp.voeg_afhankelijkheid_toe(netwerk, "Manufacturer", "Detailer", 10)
        succes = bvp.levert_indirect_aan(netwerk, "Farm A", "Refinery W") is True
    except Exception as e:
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)


def run_all_tests():
    bvp = importlib.import_module('bvp_practicum2')
    print('###')
    print('Testen voor functie voeg_bedrijf_toe en is_bedrijf:')
    test_bedrijf_toevoegen(bvp)
    print('###')
    print('Testen voor functie voeg_afhankelijkheid_toe en levert_aan:')
    test_afhankelijkheid_toevoegen(bvp)
    print('###')
    print('Testen voor functie uitstroomsnelheid_goederen:')
    test_uitstroomsnelheid(bvp)
    print('###')
    print('Testen voor functie grootste_leveraars:')
    test_grootste_leveraars(bvp)
    print('###')
    print('Testen voor functie instroomsnelheid_goederen:')
    test_instroomsnelheid(bvp)
    print('###')
    print('Testen voor functie levert_indirect_aan:')
    test_levert_indirect_aan(bvp)
    print('###')

    print('###')
    print('CUSTOM TESTS')
    print('###')
    print('Testen custom_test_bedrijf_duplicaat')
    custom_test_bedrijf_duplicaat(bvp)
    print('###')
    print('Testen custom_test_bedrijf_duplicaat_geen_verandering')
    custom_test_bedrijf_duplicaat_geen_verandering(bvp)
    print('###')
    print('Testen custom_test_geen_afhankelijkheid')
    custom_test_geen_afhankelijkheid(bvp)
    print('###')
    print('Testen custom_test_afhankelijkheid_duplicaat')
    custom_test_afhankelijkheid_duplicaat(bvp)
    print('###')
    print('Testen custom_test_afhankelijkheid_juiste_volgorde')
    custom_test_afhankelijkheid_juiste_volgorde(bvp)
    print('###')
    print('Testen custom_test_afhankelijkheid_onbestaande_bedrijven')
    custom_test_afhankelijkheid_onbestaande_bedrijven(bvp)
    print('###')
    print('Testen custom_test_uitstroomsnelheid_onbestaand_bedrijf')
    custom_test_uitstroomsnelheid_onbestaand_bedrijf(bvp)
    print('###')
    print('Testen custom_test_instroomsnelheid_onbestaand_bedrijf')
    custom_test_instroomsnelheid_onbestaand_bedrijf(bvp)
    print('###')

def main():
    run_all_tests()


if __name__ == "__main__":
    main()