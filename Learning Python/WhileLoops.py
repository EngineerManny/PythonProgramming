# while loops = a statement that will execute its block of code, as long as it's conditions remains true.

#while 1==1:
   #name = print("Help! I'm stuck in a loop!")

# name = "" 
name = None

# while len(name) == 0: 
while not name:
    name = input("Enter your name: ")

print("Hello " + name)