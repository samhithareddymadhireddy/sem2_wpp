listt=[]
import random
for i in range(0,10):
    listt.append(random.randrange(0,2))
    print(listt[i], end=' ')

print("\n")

count=[]

for i in range(0,50):
    count.append(0)

j=0

for i in range(0,9):
    if(listt[i]^listt[i+1]==0):
        count[j]+=1
    
    else:
        j+=1

print(max(count)+1)


