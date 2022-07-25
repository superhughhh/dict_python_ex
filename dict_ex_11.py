#coding: utf-8
#
#input dict{"name of student": [classnote list]}
#output dict{"name of student": classnote average}


from numpy import mean

d = {"Aladin": [12, 15 , 17] , "Nathalie" : [15, 13 , 16] , "Robert": [13, 15 , 11] }

for eleve in d:
    a = d.get(eleve)
    avg = mean(a)
    avg = round(avg,2)
    print(avg)
    d[eleve]=avg
    
print(d)
    
    

