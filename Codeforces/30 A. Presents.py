'''

    if(str(i) in n):
        
        print(n[i])
n=[1, 2, 3, 5, 3, 1, 2, 1, 6]
for i in [i for i,x in enumerate(n) if x == 1]:
    print(i)

testlist = [1,2,3,5,3,1,2,1,6]
for position, item in enumerate(testlist):    
    if(item==i+1):
'''
a=int(input())
n=[int(x) for x in input().split()]
y=''
for l in range(len(n)):
    if(l+1 in n):
        for i, j in enumerate(n):
            if(j==l+1):
                y=y+str(i+1)+' '
    else:
        y=y+n[l]+' '
print(y)                
                


