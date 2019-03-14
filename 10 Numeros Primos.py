import math
n = int(input())
raiz = int(math.sqrt(n))
flag = 1
for i in range(2,raiz+1):
    if(n%i==0):
        flag = 0
if(flag==0):
    print('No es primo')
else:
    print ('Es primo')
    
    
        
