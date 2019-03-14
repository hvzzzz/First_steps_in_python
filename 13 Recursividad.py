def suma(n):
    if(n==0):#caso base
        return 0
    else:
        return n+suma(n-1)
n = int(input())
print (suma(n))
