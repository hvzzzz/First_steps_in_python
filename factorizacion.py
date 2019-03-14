import math
n = int(input())
lim = int(math.sqrt(n))
for i in range(2, lim+2):
    cnt = 0
    while(n%i==0):
        cnt = cnt + 1
        n = n // i
    if(cnt>0):
        print (i, "^", cnt)
if(n!=1):
        print(n,'^',1)
