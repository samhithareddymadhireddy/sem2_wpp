x=int(input("enter feet"))

n=int(input("enter option"))

conversion=[x*12,x//3,x/5280,x*304.8,x*30.48,x*3.048,x*0.3048]
print(conversion[n-1])