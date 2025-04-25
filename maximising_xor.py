l=int(input("enter 1st number"))
r=int(input("enter 2nd number"))

maxx=-9999

for i in range(l,r+1):
    for j in range(i,r+1):
        if i^j>maxx:
            maxx=i^j


print(maxx)