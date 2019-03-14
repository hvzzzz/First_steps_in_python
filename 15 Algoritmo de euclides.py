def mcd(n,m):
    if(n%m==0):
        return m
    else:
        return mcd(m,n%m)
n = int(input())
m = int(input())
print (mcd(n,m))
