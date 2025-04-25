t=int(input("enter no.of test cases"))

for i in range(t):
    a=int(input("enter no.of cuts"))
    if a%2==0:
        print((a//2)**2)
    else:
        print(((a//2)**2)+a//2)