

n_list = [3, 4, 5, 6, 7, 8, 9 ,11, 12, 13]
d = {}
for n in n_list:
    divisors = []
    for i in range(1 , n + 1):
        if ( n%i == 0 ):
            divisors.append(i)
    d[n] = divisors
   
    

print(d)

    