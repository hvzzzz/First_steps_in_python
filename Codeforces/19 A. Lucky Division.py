def convertlist(i):
    a = []                       
    for h in range(len(str(i))):#este modulo convertira las cifras de 'i' en  
        a.append(i%10)          #una lista,el ultimo elemento serà i%10 y cada vez se 
        i=i//10                 #actualizara 'i' a i//10
    return a
n = int(input())
x = 'NO'    
for i in range(2,n+1):
    if(n%i==0):
        a=convertlist(i)
        y = 0
        for l in range(len(a)):
            if(a[l]==4 or a[l]==7):
                y = y+1
        if(y==len(a)):
            #print(i)    
            x = 'YES'
            break                 
print(x)                
        


  
    

