students = ["Jay", "Riya", "Amit", "Neha"]

find = input("Enter name : ")

flag = False

for x in students:
    if x == find:
        flag = True
        break

if flag:
    print("Found")
else:
    print("Not Found")