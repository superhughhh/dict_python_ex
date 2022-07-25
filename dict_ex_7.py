
#input : int list 
# output : dict { "int" : "prime/not Prime"}

n_list = [3, 4, 5, 6, 7, 8, 9 ,11, 12, 13]
d = {}
for n in n_list:
    s = "premier"
    numberDivisors = 0
    for i in range(1 , n + 1):
        if ( n%i == 0 ):
            numberDivisors += 1
    if (numberDivisors > 2):
        s = 'non premier'
    d[n] = s
   
    

print(d)

    
    