# Q2.
d={}

p='y'

while p=='y' or p=='Y':

    pro=str(input("Enter the product name"))

    d[pro]=float(input("Enter the price of the product"))

    p=input("do you want to enter more products?if yes enter y or else enter n")


    p='y'

while p=='y' or p=='Y':

    p_name=str(input("Enter the product to search"))

    if p_name==pro:

        print(p_name,d[p_name])

    else:

        print("The product is not present")

p=input("do you want more products to search?(y/n)")