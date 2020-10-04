volume = 0
zijde = -1
vorige_zijde = -1

while zijde != 0:
    zijde = int(input())
    if zijde > vorige_zijde:
        volume = 0
    if zijde > 0:
        volume += zijde * zijde
    vorige_zijde = zijde


print(volume)