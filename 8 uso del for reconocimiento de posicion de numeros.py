pair = 0
odd = 0
n = int(input())
for i in range(n):
    h = int(input())
    if(i%2==0):
        odd=odd+h
    else:
        pair=pair+h
print(pair)
print(odd)
