#coding utf-8
"""Ecrire un programme Python qui permet de créer à partir d'un entier entier n saisi au clavier , un dictionnaire formé des entiers de 1 à n et de leurs carrées. Exemple pour n = 7 le dictionnaire sera de la forme:"""


def addSquareNumber(d):
    n = int(input("Saisir un nombre"))
    d.update({n : n**2})
    return d

square_dict = {}

addSquareNumber(square_dict)
addSquareNumber(square_dict)
print(square_dict)