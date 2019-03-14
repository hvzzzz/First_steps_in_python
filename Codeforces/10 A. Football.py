n=input()
n=[int(n) for n in n]#esto convertira los elementos de la lista en enteros
count=0
if(len(n)<7):
    print('NO')
else:    
    for i in range(len(n)):
        if(i<len(n)-6):
            if(n[i]==n[i+1]):
                if(n[i+1]==n[i+2]):
                    if(n[i+2]==n[i+3]):
                        if(n[i+3]==n[i+4]):
                            if(n[i+4]==n[i+5]):
                                if(n[i+5]==n[i+6]):
                                    count=1
                                    i=len(n)-6                            
    if(count==1):
        print('YES')
    else:
        print('NO')
        
        
