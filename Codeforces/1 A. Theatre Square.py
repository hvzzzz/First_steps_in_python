n, m, a = map(int, input().split())
Largo=m//a
Ancho=n//a
if(m%a!=0):
    Largo=Largo+1
if(n%a!=0):
    Ancho=Ancho+1
print(Largo*Ancho)
