pair = 1
odd = 1
count = 0
n = int(input())
for i in range(n):
    h = int(input())
    if(h%2==0):
        pair=pair*h       
    else:
        odd=odd*h
        if(h==1):
            count = count+1
if(count>0 and odd==1):
    odd = 1
if(count==0 and odd==1):
    odd = 0
if(pair==1):
    pair = 0
print(pair)
print(odd)

        
        
