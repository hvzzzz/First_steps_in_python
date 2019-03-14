n = int(input())
m = int(input())
if(n==0 or m==0):
    print('valor incorrecto')
else:
    while(n%m!=0):
        aux = m
        m = n%m
        n = aux
    print(m)    
    
