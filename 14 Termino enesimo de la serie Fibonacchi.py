def fibonacchi(n):
    if(n==1 or n==2):
        return n
    else:
        return fibonacchi(n-1)+fibonacchi(n-2)  
n = int(input())
print (fibonacchi(n))
