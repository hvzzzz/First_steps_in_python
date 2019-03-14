n = int(input())
for i in range (n):
    x = input()
    if(len(x)>10):
        answer = x[0] + str(len(x)-2) + x[len(x)-1]
        print(answer)
    else:
        print(x)
