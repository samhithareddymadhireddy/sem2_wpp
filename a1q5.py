for i in range(2):

    list.append(str(input("Enter student names")))

print("Student names reverse:")

for name in list:

    if len(name)>15:

        name=name[:15]

    reverse_name=name[::-1]


print(reverse_name)