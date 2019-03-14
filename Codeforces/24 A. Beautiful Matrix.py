a = []
r = 0
s = 0
p = 0
q = 0
for i in range(5):
    n = [int(x) for x in input().split()]
    a.append(n)
for i in range(len(a)):
    for l in range(len(a[i])):
        if(a[i][l]==1):
            r = i
            s = l            
if(r==2):
    q = 0
if(r<2):
    q = -r+2    
if(r>2):
    q = r-2
if(s==2):
    p = 0
if(s<2):
    p = -s+2
if(s>2):
    p = s-2    
print(p+q)    
