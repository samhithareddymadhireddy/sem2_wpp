x=[]
y=[]
z=[]
points=[]
for i in range(3):
    x.append(int(input("enter x")))
    y.append(int(input("enter y")))
    z.append(int(input("enter z")))

    points.append(x[i])
    points.append(y[i])
    points.append(z[i])

#print(points)
subresult=[0,0,0]
result=[]
#min=9999
for i in range(0,3):
    min=9999
    for j in range(i+1,3):
        
        dist=(x[i]-x[j])**2+(y[i]-y[j])**2+(z[i]-z[j])**2
        if(dist<min):
            min=dist
            a=i
            b=j
    
    subresult[0]=x[a]
    subresult[1]=y[a]
    subresult[2]=z[a]
    result.append(subresult)
    print(result)
    # subresult[0]=x[b]
    # subresult[1]=y[b]
    # subresult[2]=z[b]
    # result.append(subresult)

print(result)





