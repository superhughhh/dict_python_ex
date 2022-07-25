#coding utf-8
"""input : int(n)
    output : dictionary key : 1, 2, 3, ...,n // values : 1, 1+2, 1+2+3, ...,+n"""



def dicRange():
    dict = {}
    v = 0
    nombre = int(input("entrez un int"))
    for i in range(1, nombre +1):
        v += i
        dict[i] = v
    return dict

a = dicRange()
print(a)
