def suma(a,n):
    if(n==-1):
        return 0
    else:
        return a[n]+suma(a,n-1)
if __name__ == '__main__':
    a=[]
    n=int(input())
    for i in range(n):
        x = int(input())
        if(i%3!=0):
            x=-x
        a.append(x)
    print(suma(a,n-1))    
#Aqui otro metodo de solución
def suma(a,n,state):
    if(n==-1):
        return 0
    if(state==1 or state==2):
        return -a[n]+suma(a,n-1,(n+2)%3)#esta formula convertira n de 0 a 2 y 1
    else:
        return a[n]+suma(a,n-1,(n+2)%3)
if __name__ == '__main__':
    a=[]   
    n=int(input())
    state=(n-1)%3#esta es la formula general para n
    for i in range(n):
        x = int(input())
        a.append(x)
    print(suma(a,n-1,state))    
