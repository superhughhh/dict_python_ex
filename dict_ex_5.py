"""Écrire un programme en Python qui demande à l'utilisateur de saisir une une chaine de caractère, et de lui renvoyer un dictionnaire dont les clés sont les caractères de la chaine saisie et les valeurs sont les nombres d’occurrences des caractères dans la chaine. Exemple pour la chaine s = "langage" , le programme renvoie le dictionnaire:"""


def addSquareNumber(d,s):
    for l in s:
        x = s.count(l)
        print(x)
        d.update({l : x})
    return d

count_character = {}
str = "Langage"

addSquareNumber(count_character, str)
print(count_character)