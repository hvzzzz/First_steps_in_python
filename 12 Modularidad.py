def Suma(a,b):
    return a+b
a = int(input())
b = int(input())
print(Suma(a,b))
#el problema numero 11 seria de la siguiente manera:
def factorizar(n):
    import math
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
x = int(input())
factorizar(x)
    

