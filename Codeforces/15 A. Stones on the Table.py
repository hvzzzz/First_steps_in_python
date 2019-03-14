n = int(input())
s = input()
s = list(s)
x = 0
for i in range(n):
    if(i<n-1):
        if(s[i]==s[i+1]):
            x = x+1
print(x)        
