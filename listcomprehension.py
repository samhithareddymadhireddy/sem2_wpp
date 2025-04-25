
x=int(input("enter feet"))

n=int(input("enter option"))

conversion=[x*12 if n==1 else x//3 if n==2 else x/5280 if n==3 else x*304.8 if n==4 else x*30.48 if n==5 else x*3.048  if n==6 else x*0.3048] 
print(conversion)

