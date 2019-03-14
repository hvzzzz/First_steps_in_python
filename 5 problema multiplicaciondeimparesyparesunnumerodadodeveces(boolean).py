pair = 1
odd = 1
flag = true
n = int(input())
for i in range(n):
    h = int(input())
    if(h%2==0):
        pair=pair*h       
    else:
        odd=odd*h
        flag = false
if(pair==1):
    pair = 0
if(flag):
    odd = 0
print(pair)
print(odd)
#la variable flag es un boolean si entra a la parte del codigo donde el caso es impar se volvera false y eso nos indicara si hubo algun impar en los numeros dados
#tambien se pueden intercambiar las posiciones del true and false
pair = 1
odd = 1
flag = false
n = int(input())
for i in range(n):
    h = int(input())
    if(h%2==0):
        pair=pair*h       
    else:
        odd=odd*h
        flag = true
if(pair==1):
    pair = 0
if(!flag):
    odd = 0
print(pair)
print(odd)
#esto teniendo en cuenta la condicion final en la que se chequea si aparecio algun impar
