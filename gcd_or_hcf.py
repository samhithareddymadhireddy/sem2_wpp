# finding gcd(hcf)

# def hcf( n1, n2):
#     if (n2 != 0):
#         return hcf(n2, n1 % n2)
#     else:
#         return n1
# n = int(input("Enter the first number"))
# m = int(input("Enter the second number"))
# print("The GCD of numbe is",hcf(n,m))


# lcm
n1,n2=12,18
lcm=max(n1,n2)
print(lcm)
maxx=lcm

while lcm%n1!=0 or lcm%n2!=0:
    lcm+=maxx

print("lcm is",lcm)

             