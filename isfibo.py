def isFibo(n):
    a,b=0,1
    while a<n:
        a,b=b,a+b
        if a==n:
            return True
        
    return False
    #return a==n

N=int(input("enter number"))
if isFibo(N):
    print("isFibo")
else:
    print("not fibo")

