a= input()
a=list(a)#
b=''
for i in range(len(a)):       
    if(ord(a[i])>=ord('A')and ord(a[i])<=ord('Z')):
        a[i]=chr(ord(a[i])+32)      
    if(a[i]=='a' or a[i]=='o' or a[i]=='y' or a[i]=='e' or a[i]=='u' or a[i]=='i'): 
        a[i]=''
    if(a[i]!=''):
        b=b+'.'+a[i]    
print(b)


        
