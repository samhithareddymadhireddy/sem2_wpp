s=input("enter string")

letters=set(s)
if len(letters)<27:
    print("not a pangram")

else:
    print("is a pangram")