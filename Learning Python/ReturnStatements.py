# return statement = Funtions send Python values/objects back to the caller. These values/objects are known as the funtions return value

def multiply(num1, num2):
    result = num1 * num2
    return result

# a shorter way to return
def division(num1, num2):
    return num1 / num2

x = multiply(10,4)
y = division(55,5)

print(x)
print(y)