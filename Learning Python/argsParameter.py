# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

# example of a program that only accepts 2 arguments becuase it has only 2 paramters
# anything less than 2 or greater than 2 will cause an issue. 
def add(num1, num2):
    return num1 + num2 

print(add(1,2))

def add(*args):
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6,7,8,9))