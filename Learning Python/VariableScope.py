# scope = The region that a variable is recognized
#         A variable is only available from inside the region that is it created
#         A global and locally scoped versions of a variable can be created
# Python uses the LEGB rule in that order
# L = Local
# E = Enclosing
# G = Global
# B = Built-in

name = "Manny"        # global scope (available inside and outside functions)

def display_name():
    name = "Manny"    # local scope (available only inside this function)
    print(name)

display_name()
print(name)