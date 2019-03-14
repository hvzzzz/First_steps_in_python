n = input()
n = list(n)
for i in range(len(n)):
    if(n[i]=='H' or n[i]=='Q' or n[i]=='9'):
        print('YES')
        break
else:
    print('NO')
