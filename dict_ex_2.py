#coding utf-8
# 3 differents technics to concatenate 3 dict in 1

dicPC={"HP": 11 , "Acer": 7 , "Lenovo": 17 , "Del": 23}
dicPhone={"Sumsung": 22 , "Iphone": 9 , "Other": 13 }
dicTablette = {"Sumsung": 15 , "Other": 13}

newdict = {}
list_dict = [dicPC, dicPhone, dicTablette]
for i in list_dict:
    for y in i:
        newdict[y] = i.get(y)
        
print(newdict)

new_dict2 = {}
for d in list_dict:
    new_dict2.update(d)
    
print(new_dict2)
    
    
new_dict3 = {}
new_dict3.update(dicPC)
new_dict3.update(dicPhone)
new_dict3.update(dicTablette)
print(new_dict3)