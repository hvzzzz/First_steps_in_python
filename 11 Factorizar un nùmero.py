import math
n = int(input())
raiz = int(math.sqrt(n))
for i in range(2,raiz+2):   
    count = 0
    while(n%i==0):
        count = count+1
        n=n//i
    if(count>0):
        print(i,'^',count)    
if(n!=1):
        print(n)            
    
