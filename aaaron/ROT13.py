lijst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

woord = input("geef woord: ")
nieuw_woord = ""
for letter in woord:
    index = 0
    for i in range(len(lijst)):
        if lijst[i] == letter:
            index = i
    if index < 13:
        nieuw_woord += lijst[index + 13]
    else:
        nieuw_woord += lijst[index - 13]

print(nieuw_woord)
