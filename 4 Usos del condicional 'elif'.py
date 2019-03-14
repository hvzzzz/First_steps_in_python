n = int(input('Ingrese el numero de veces que desea ejercutar:'))
for i in range(n):
    A, B = map(int, input('Ingrese los numeros:').split())
    if(A>B):
        print('>')
    elif(A<B):
        print('<')
    else:#(A==B)
        print('=')
