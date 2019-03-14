#n = int(input())
#for i in range(n):
    #if(n%i==0):
        #print(i)
#el codigo de arriba escribira los divisores de un número,pero es muy lento, para optimizarlo
#se hace el codigo de abajo        
import math
n = int(input())
raiz = int(math.sqrt(n))
for i in range(1,raiz+1):
    if(n%i==0):        
        print(i)
        if(i!=n//i):
            print(n//i)
#se importa la bibliote de math (esta contiene varios operadores matematicos)
#la idea es la siguiente:
            #se saca la raiz cuadrada del numero y solo se revisa hasta ese numero
            #con cada divisor que se obtuvo de allí de divide el numero n
            #el resultado de cada interaccion sera tambien divisor de n
            
#la variable raiz se plantea como entero ya que for i in range solo soporta enteros
#raiz contiene el resultado de la raiz cuadrada de n

#la segunda condicional corregira el caso de los cuadrados perfectos
#si i == n//i nos escribira como resultado 2 veces el mismo divisor(solo cuadrados perfectos)
#para ello se pone la condicion de que i siempre debe ser distinto de n//i
            
            
       
       
        
