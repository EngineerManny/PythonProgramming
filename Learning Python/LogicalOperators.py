# Logical Operators (and, or, not) = used to check if two or more conditional statements are true
# And - Used in an if statement to proceed if both conditions are met.
# Or - Used in an if statement to proceed if either of the coniditions are met.
# Not - Used in an if statementment to flip true to false or false to true. 

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside!")

#if not(temp >= 0 and temp) <= 30:
    #print("The temperature is bad today!")
    #print("Stay inside!")
#elif not(temp < 0 or temp) > 30:
    #print("The temperature is good today!")
    #print("Go outside!")
    
