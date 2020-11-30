import string


def clean_word(w):
    return w.lower().strip(string.punctuation)


def print_voc(s):
    x = s.split()
    blub = set()
    for word in x:
        blub.add(clean_word(word))
    print(blub)
    return


print_voc("crazy humburger hamburger is CRAZY")
