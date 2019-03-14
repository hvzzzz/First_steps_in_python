k, n, w= map(int,input().split())
x=0
for i in range(1,w+1):
    x=x+i*k
if(x>n):
    print(x-n)
else:
    print('0')
