n = int(input())
x = 0
for i in range(n):
    a=input()
    a=list(a)
    for l in range(len(a)):
        if(l!=(len(a)-1)):
            if(a[l]=='+' and a[l+1]=='+'):
                x = x+1       
            if(a[l]=='-' and a[l+1]=='-'):
                x = x-1
print(x)
        
