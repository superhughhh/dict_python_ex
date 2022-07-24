#some basics function to edit dictionary

"""1) Corriger l'erreur "stockage": "750 G"
2) Créer un programme qui affiche la liste des clés, la liste des valeurs
et la liste des paires de clés et valeurs
3)Inverser les paires "processeur": "Intel core i5" et "stockage": "500 G"
4) Ajouter la pair clé-valeur : "Système d'exploitation" : "Windows 10"""


mydict = {"device": "laptop" , "constructeur": "acer" , "ram": "8G" , 
"processeur": "Intel core i5", "stockage": "500 G"}

mydict["stockage"] = "750G"
print(mydict.keys())
print(mydict.values())
print(mydict.items())
mydict.pop("processeur")
mydict.update({"processeur": "Intel core i5"})
mydict["Système d'exploitation"] = "Windows 10"
print(mydict.items())
