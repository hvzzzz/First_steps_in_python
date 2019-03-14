a = input()
a = list(a)
lz = [0]*128
x = 'IGNORE HIM!'
y = 0 
for i in range(len(a)):
    lz[ord(a[i])]=lz[ord(a[i])]+1
for i in range(len(lz)):
    if(lz[i]!=0):
        y=y+1
if(y%2==0):
    x='CHAT WITH HER!'
    print(x)
else:
    print(x)
    
    
    

    
