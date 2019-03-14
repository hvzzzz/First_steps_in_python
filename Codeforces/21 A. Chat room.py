n = input()
n = list(n)
x = 'NO'
for i in range(len(n)):
    if(n[i]=='h'):
        for a in range(i+1,len(n)):
            if(n[a]=='e'):
                for b in range(a+1,len(n)):
                    if(n[b]=='l'):
                        for c in range(b+1,len(n)):
                            if(n[c]=='l'):
                                for d in range(c+1,len(n)):
                                    if(n[d]=='o'):
                                        x='YES'
print(x)                                        
