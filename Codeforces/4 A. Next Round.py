n, k = map(int, input().split())
a = [int(x) for x in input().split()] #covierte una linea de numeros en una lista
count=0
for i in range(len(a)):    
    if(a[i]>=a[k-1] and a[i]>0):
        count=count+1
print(count)        
