n = int(input())
x = [int(x) for x in input().split()]
ans = 0
a = 0
b = 0
c = 0
d = 0 
for i in range(len(x)):
    if(x[i]==1):
        a = a+1
    if(x[i]==2):
        b = b+1
    if(x[i]==3):
        c = c+1
    if(x[i]==4):
        d = d+1
case1=min(a,c)
ans=ans+case1
a=a-case1
c=c-case1

ans=ans+c

case2=b//2
ans=ans+case2
b=b%2

if(b==1):
    a=a-min(a,2)#se elige dos ya que al ser 'a' 2 siempre se restara 2 en su actualizacion, pero si 'a' es menor que 2 solo se formara un grupo con 'b' y se actualizaria con su mismo valor de 'a' 
    b=0
    ans=ans+1
ans=ans+a//4+(0 if a%4==0 else 1)    
print(ans+d)    
    

            
