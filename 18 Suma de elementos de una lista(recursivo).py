def suma(a,n):
    if(n==-1):
        return 0
    else:
        return a[n]+suma(a,n-1)
if __name__ == '__main__':#esta linea marcará el inicio de la parte principal del codigo
    a=[]
    n=int(input())
    for i in range(n):
        x = int(input())
        a.append(x)
    print (suma(a,n-1))    



