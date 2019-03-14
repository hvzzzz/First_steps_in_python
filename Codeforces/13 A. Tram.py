n = int(input())
x = 0
h = []
for i in range(n):
    a, b=map(int, input().split())
    x = x+b-a    
    h.append(x)
print(max(h))    
