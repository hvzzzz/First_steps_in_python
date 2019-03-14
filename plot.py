import numpy as np
import matplotlib.pyplot as plt
import math as m

# Fixing random state for reproducibility
a,b,d,n1,n2=2,4,5,1,2
c=300000000
x= np.linspace(2.0, 100.0, num=100)
t= np.linspace(2.0, 100.0, num=100)
#print(t)
for i in range (100):
    t[i]=(n1*m.sqrt(m.pow(x[i],2)+m.pow(a,2))/c)+(n2*m.sqrt(m.pow(d-x[i],2)+m.pow(b,2))/c)
#x = mu + sigma * np.random.randn(10000)
# the histogram of the data
plt.hist( t,1, normed=1, facecolor='g', alpha=0.99)
 
plt.xlabel('Posicion')
plt.ylabel('Tiempo')
plt.title('Comportamiento de la Funcion')
plt.axis([2, 100, 3, 10])
plt.grid(True)
plt.show()
#print(x)
#print(t)
