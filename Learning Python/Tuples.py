# tuple = collection which is ordered and unchangeable used to group together related data

student = ("Manuel", "19", "Male")

print(student.count("Manny"))
print(student.index("Male"))

for x in student:
    print(x)

if "Manny" not in student:
    print("Manny is not here!")