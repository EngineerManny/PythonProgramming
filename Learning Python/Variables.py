# Variable - A container for a value. Behaves as the vaue that it contains.
    #String - A variable that is made up of different alphabetical letters.
    #Int - A variable that only contains whole numbers, and integers while not allowing decimals.
    #Float - A vairaible that contains whole numbers, integers, and decimals.
    #Boolean - A variable that can either be true or false.

name = "Manny"
print(type(name))
print("Hello "+name)

First_name = "Manny"
Last_name = "Tapia"
Full_name = First_name +" "+ Last_name
print("Hello "+Full_name)
print(type(Full_name))

age = 21
age = age + 1
#another way to add 1 is to do:
age += 1
age += 1
print(age)                                                                                                                                                             
print(type(age))
print("Your age is " + str(age))

height = 250.5
print("You are " + str(height) + "cm " + "tall.")
print(type(height))

Human = True
print(Human)
print(type(Human))
print("Are you a human? " + str(Human))