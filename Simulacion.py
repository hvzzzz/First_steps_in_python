import numpy as np
import matplotlib.pyplot as plt
import math as m
print('Ingrese el valor de "a" y presione la tecla enter')
a=int(input())
print('Ingrese el valor de "b" y presione la tecla enter')
b=int(input())
print('Ingrese el valor de "d" y presione la tecla enter')
d=int(input())
print('Ingrese el valor de del Indice de Refraccion del Primer Medio y presione la tecla enter')
n1=float(input())
print('Ingrese el valor de del Indice de Refraccion del Segundo Medio y presione la tecla enter')
n2=float(input())
#a,b,d,n1,n2=50,40,50,1,2# valores de prueba usados en el ejemplo
c=299792458
x= np.linspace(-100.0, 100.0, num=1000000)#creacion del arreglo de las 'x's
t= np.linspace(-100.0, 100.0, num=1000000)#creacion del arreglo de las 't's
for i in range (1000000):
    t[i]=(n1*m.sqrt(m.pow(x[i],2)+m.pow(a,2))/c)+(n2*m.sqrt(m.pow(d-x[i],2)+m.pow(b,2))/c)# modificacion del arreglo de las 't's usando la formula dada en clase   
plt.xlabel('Posicion')
plt.ylabel('Tiempo')
plt.title('Comportamiento de la Funcion T(x)')    
plt.plot(x, t, 'r--')
plt.show()
print('Tiempo minimo:')
print (np.amin(t))
print('Posicion del tiempo minimo(x minimo):')
print(x[list(t).index(np.amin(t))])