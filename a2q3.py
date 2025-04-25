T=int(input("Enter number of test cases"))

N=[]

count=0


for i in range(0,T):

    N.append(int(input("Enter the number")))

for i in range(T):

    k=N[i]

while(k!=0):

    q=k%10

    if q>0 and N[i]%q==0:

        count+=1

    k=k//10

    print(count)

    count=0