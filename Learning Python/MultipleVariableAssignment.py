#Multiple assignment - Allows us to assignment multiple varibales at the same time in one line of code. 

name = "Manny"
age = 19
smart = True

name, age, smart = "Manny", 19, True

print(name)
print(age)
print(smart)

Dawelny = 25
William = 25
Jarahn = 25
Javont = 25

#or mupltiple assignemnt

Dawelny = William = Jarahn = Javont = 25
print(type(Dawelny))
print("Your friends Dawelny, William, Jarahn, and Javont are all " + str(William) + " years old.") 

