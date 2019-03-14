n = input()
n = list(n)
x=0
y=''
for i in range(len(n)):
    if(i!=0):
        if(ord(n[i])>=ord('A') and ord(n[i])<=ord('Z')):                     
            x = x+1          
if(len(n)>1): 
    if(x==len(n)-1):
        if(ord(n[0])>=ord('a') and ord(n[0])<=ord('z')):
            n[0]=chr(ord(n[0])-32)
            y = y + n[0]
        else:
            n[0]=chr(ord(n[0])+32)
            y = y + n[0]
        for i in range(len(n)):                    
            if(i!=0):
                if(ord(n[i])>=ord('A') and ord(n[i])<=ord('Z')):
                    n[i]=chr(ord(n[i])+32)
                    y = y + n[i]
                else:
                    n[i]=chr(ord(n[i])-32)
                    y = y + n[i]         
        print(y)
    if(x<len(n)-1):
        for i in range(len(n)):
            y = y + n[i]
        print(y)    
else:
    if(ord(n[0])>=ord('a') and ord(n[0])<=ord('z')):
        n[0]=chr(ord(n[0])-32)
        y = y + n[0]
    else:
        n[0]=chr(ord(n[0])+32)
        y = y + n[0]
    print(y)    
