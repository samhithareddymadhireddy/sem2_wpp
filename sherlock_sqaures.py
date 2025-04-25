
a=int(input("enter lower range"))
b=int(input("enter upper range"))



square=0
for i in range(a,b+1):
    j=1
    count=0
    while(j<=i):
        if i%j==0:
            count+=1
        j+=1

    if count%2!=0:
        square+=1

        
print(square)
