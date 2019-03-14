n = input()
n = list(n)
a = input()
a = list(a)
for i in range(len(a)):       
    if(ord(a[i])>=ord('A')and ord(a[i])<=ord('Z')):
        a[i]=chr(ord(a[i])+32)          
    if(ord(n[i])>=ord('A')and ord(n[i])<=ord('Z')):
        n[i]=chr(ord(n[i])+32)
for i in range(len(n)): 
    if(a[i]>n[i]):        
        print(-1)
        break
    if(ord(a[i])<ord(n[i])):
        print(1)
        break
if(a==n):
    print(0)
            
