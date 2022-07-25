#coding: utf-8
#this program allows to remove duplicate contents in dictionary
 
students = {'id1':  {'name': 'Catherine' , 'section': 'SVT', 'age': 17},
                'id2':  {'name': 'Majid' , 'section': 'Math', 'age': 18},
                'id3':  {'name': 'Catherine' , 'section': 'SVT', 'age': 17},
                'id4':  {'name': 'Robert' , 'section': 'Physique', 'age': 19}
                }
 
# I initialize a new dict
remove_duplicate = dict({})
 
# I browse a dictionary
for key , data in students.items():
    
    # I rebuild a dictionary without duplicate
    if data not in remove_duplicate.values():
        remove_duplicate[key] = data
        
        
print(remove_duplicate)
# affiche: 
""" 
{'id1': {'name': 'Catherine', 'section': 'SVT', 'age': 17}, 
'id2': {'name': 'Majid', 'section': 'Math', 'age': 18}, 
'id4': {'name': 'Robert', 'section': 'Physique', 'age': 19}}
"""