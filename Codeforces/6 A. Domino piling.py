M, N =map(int, input().split())
if(M%2==0):
    print((M//2)*N)
if(M%2!=0):
    print((M//2)*N+(N//2))
