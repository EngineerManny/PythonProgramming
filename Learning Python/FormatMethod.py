# str.format() = optional method that gives users
#                more control when displaying output

#Character = "Humpty Dumpty"
#item = "wall"

#print(Character, "sat on the", item + "!")
#print("{} sat on the {}".format(Character, item))
#print("{1} sat on the {0}".format(Character, item)) # Postional Arguments
#print("{1} sat on the {0}".format(item, Character)) # Postional Arguments
#print("{Character} sat on the {Item}.".format(Character="Humpty Dumpty", Item="wall")) # Keyward Arguments

#text = "{} sat on the {}"
#print(text.format(Character, item))

#name = "Manny"

#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}. Nice to meet you!".format(name))
#print("Hello, my name is {:<10}. Nice to meet you!".format(name))
#print("Hello, my name is {:>10}. Nice to meet you!".format(name))
#print("Hello, my name is {:^10}. Nice to meet you!".format(name))

pi = 3.14159
number = 1000

print("The number pi is {:.2f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:x}".format(number))
print("The number is {:X}".format(number))
print("The number is {:e}".format(number))
print("The number is {:E}".format(number))