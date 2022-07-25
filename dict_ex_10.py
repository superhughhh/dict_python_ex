#be careful to be in local folder with terminal(dict_python_exercice)
#this progam allows to the name of the file and its number of line in dictionary in repository

from shell import shell

dict = {}

ls = shell('ls')
for file in ls.output():
    
    with open(file, "r") as f:
        lines = f.readlines()
        
    count = 0
    for line in lines:
        count += 1
    dict[file]=count
print(dict)

