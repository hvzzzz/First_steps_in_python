n = int(input())
a = map(int, input().split())
a = list(a)
a.sort()
x = 0
y = 0
val = 0
for i in range(len(a)):
    val = val+a[i]   
for i in range(len(a)-1,-1,-1):
    if(x<=val/2):
        x=x+a[i]
        y=i
    else:
        break
print(len(a)-y)

        
