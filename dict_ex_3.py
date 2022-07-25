#coding utf-8



etudiants = {"etudiant_1" : 13 , "etudiant_2" : 17 , "etudiant_3" : 9 , "etudiant_4" : 15 , 
			 "etudiant_5" : 8 , "etudiant_6" : 14 , "etudiant_7" : 16 , "etudiant_8" : 12 , 
			 "etudiant_9" : 13 , "etudiant_10" : 15 , "etudiant_11" : 14 , "etudiant_12" : 9 , 
			 "etudiant_13" : 10 , "etudiant_14" : 12 , "etudiant_15" : 13 , "etudiant_16" : 7 ,
			 "etudiant_17" : 12 , "etudiant_18" : 15 , "etudiant_19" : 9 , "etudiant_20" : 17 ,}

etudiantAdmis = {}
etudiantNonAdmis = {}

for e in etudiants:
    v = etudiants.get(e)
    if v >= 10:
        etudiantAdmis[e] = etudiants.get(e)
    else:
        etudiantNonAdmis[e] = etudiants.get(e)


#correction version, more simple...


for key , valeur in etudiants.items():
    if(valeur < 10):
        etudiantNonAdmis[key] = valeur
    else:
        etudiantAdmis[key] = valeur