string=input("enter string")

s=list(string)

r=len(s)-1
#print(s[0],s[1])

while r>=0:
    l=r-1

    while l>=0:
        if ord(s[r])>ord(s[l]):
            s[r],s[l]=s[l],s[r]

            break

        else:
            l-=1
    if(l>=0):
        break
    r-=1

if r<0:
    print("no answer")

string2="".join(s)
print(string2)