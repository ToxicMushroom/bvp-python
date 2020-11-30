volume = 0  # variabele voor het volume van de piramide in bij te houden, geinitialiseerd op 0 omdat een piramide begint vanaf 0
zijde = -1  # variabele voor de huidige zijde in bij te houden, geinitialiseerd op -1 zodat de while lus kan beginnen
vorige_zijde = -1  # variabele om de vorige zijde in bij te houden, geinitialiseerd op -1 maar heeft niet veel effect

while zijde != 0:  # zolang dat de ingegeven zijde verschilt van 0:
    zijde = int(input())  # lees het nieuw aantal blokjes van de zijde voor de volgende laag in
    if zijde > vorige_zijde:  # als de ingegeven zijde groter is dan de vorige zijde dan beginnen we een nieuwe piramide
        volume = 0  # volume op 0 dus een nieuwe piramide
    if zijde > 0:  # als de zijde groter is dan 0
        volume += zijde * zijde  # dan verhogen we het volume met zijde * zijde aantal blokjes ( kon ook zijde**2 )
    vorige_zijde = zijde  # vorige zijde wordt nu naar de huidige zijde veranderd omdat we een nieuwe zijde in de volgende iteratie zullen opvragen

#  ingegeven zijde was 0, we zijn uit de while lus
print(volume)  # print het volume van de ingegeven piramide
