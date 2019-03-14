import numpy as np
a = np.array([9,5,3])
suma = 0
for i in range(a.size): 
    if(a[i]!=0):
        suma = suma+a[i]
print(suma)    
