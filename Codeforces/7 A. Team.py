n = int(input())
count = 0
for i in range(n):
    a, b, c =map(int, input().split())
    if((a==1 and b ==0 and c==0) or (a==0 and b ==1 and c==0) or (a==0 and b ==0 and c==1) or (a==0 and b ==0 and c==0)):
        count = count
    else:
        count = count +1
print(count)        
        
        
