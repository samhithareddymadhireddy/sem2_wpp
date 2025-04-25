t=int(input("enter number of testcases"))

listt=[]


for i in range(t):
    listt.append(int(input("enter number")))


def utopian_tree(n):
    sum=1

    for j in range(n):
        if(j%2==0):
            sum*=2
        else:
            sum+=1
    
    return sum

for k in range(t):
    val=utopian_tree(listt[k])
    print(val)

    