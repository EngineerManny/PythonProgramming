# keyword arguemetents = arguements preceeded by an identifier when we pass them to a function.
#                        The order of the arguments doesn't matter, unlike posiontional arguments
#                        Python knows the names of the arguments that our function receives

# example of a positional arguments

def Hello(first, middle, last):
    print("Hello " + first + " " + middle +  " " + last)

Hello("Manny", "A.", "Tapia")
Hello("Tapia", "A.", "Manny")
Hello(middle = "A.", last = "Tapia", first = "Manny")
