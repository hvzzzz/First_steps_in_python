n, t = map(int, input().split())
s = input()
s = list(s)
x = ''
for i in range(t):
    for l in range(n):
        if(l<n-1):        
            if(s[l]=='B' and s[l+1]=='G'):             
                x=x+'G'+'B'
                s[l]='0'
                s[l+1]='0'
                if(l==len(s)-2):
                    break   
            else:
                if(s[l]!='0'):
                    x=x+s[l]
                    s[l]='0'
    if(s[n-1]!='0'):
        x=x+s[n-1]
        s[n-1]='0'
    s=list(x)
    if(i<t-1):
        x=''
print(x)        




