n = input()
n = list(n)
x=''
if(ord(n[0])>=ord('a') and ord(n[0])<=ord('z')):
        n[0]=chr(ord(n[0])-32)
for i  in range(len(n)):
    x=x+n[i]    
print(x)        
