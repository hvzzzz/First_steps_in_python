n = int(input())
x = 0
for i in range(n):
    p, q=map(int,input().split())
    if(p+2<=q):
        x=x+1
print(x)        
    
