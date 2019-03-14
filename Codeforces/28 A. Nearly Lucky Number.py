n = input()
n = list(n)
x = 'NO'
y = 0
for i in range(len(n)):
    if(n[i]=='4' or n[i]=='7'):    
        y=y+1
if(y==7 or y==4):
    x='YES'
print(x)    
    
    
        
