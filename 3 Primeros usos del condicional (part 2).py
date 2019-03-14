#A = int(input())
#B = int(input())
A, B = map(int, input().split())
if(A%2==0 and B%2==0):
    print(A*B)
elif(A%2==0 and B%2!=0):
    print(A//B)
elif(A%2!=0 and B%2==0):
    print(A+B)
elif(A%2!=0 and B%2!=0):
    print(A-B)
