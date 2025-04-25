n=int(input("enter no.of test cases"))

listt=[]

for i in range(n):
    listt.append(int(input("enter no.of cycles")))

for i in range(n):
    if listt[i]==0:
        print("1")
    elif listt[i]%2==0:
        print(listt[i]*2-1)
    else:
        print(listt[i]*2)
        

