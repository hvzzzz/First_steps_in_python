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
        if(i%2!=0):
            x=-x
        a.append(x)
    print(suma(a,n-1))
#Seguidamente de muestra otra solucion usando un metodo mas recursivo
def suma(a,n,state):#el tercer parametro nos indicara si es positivo o no (0 posi y 1 negativo)
    if(n==-1):
        return 0    
    if(state==0):
        return a[n]+suma(a,n-1,1)
    else:
        return - a[n]+suma(a,n-1,0)
if __name__ == '__main__':
    a=[]
    n=int(input())
    state=(n-1)%2
    for i in range(n):
        x = int(input())     
        a.append(x)
    print(suma(a,n-1,state))    
    
        
