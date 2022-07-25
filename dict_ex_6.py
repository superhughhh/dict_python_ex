


def addSquareNumber(d,s):
    len_s = len(s)
    for index in range(0, len_s):
        letter = s[index]
        d.update({letter : index})
    return d

def addSquareNumber2(d,s):
    len_s = len(s)
    for index in range(0, len_s):
        letter = s[index]
        d.update({letter : index})
    return d


count_character = {}
str = "Langage"

addSquareNumber(count_character, str)
print(count_character)