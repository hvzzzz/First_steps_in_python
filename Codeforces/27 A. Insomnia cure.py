k =int(input())
l =int(input())
m =int(input())
n =int(input())
d =int(input())
a=[0]*d
if(k==1 or l==1 or m==1 or n==1):
    a[0]=1
for i in range(k-1,len(a),k):
    a[i]=1
for i in range(l-1,len(a),l):
    a[i]=1
for i in range(m-1,len(a),m):
    a[i]=1
for i in range(n-1,len(a),n):
    a[i]=1
print(sum(a))    
