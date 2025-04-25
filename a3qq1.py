n=int(input("enter number"))

def digroot(sum):
    if sum//10==0:
        return sum
    dsum=sum
    sum=0
    while(dsum!=0):
        r=dsum%10
        dsum//=10
        sum+=r
    ans=digroot(sum)
    return ans


val=digroot(n)
print(val)

