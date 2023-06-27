#Assignment: Temperature Converter (Simplified)

#Write a Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin. Your program should have the following functionality:

#Prompt the user to enter a temperature value.
#Prompt the user to enter the temperature unit (Celsius, Fahrenheit, or Kelvin).
#Convert the entered temperature to the other two units.
#Display the converted temperatures.
#You can use the following conversion formulas:

#Celsius to Fahrenheit: F = (C * 9/5) + 32
#Celsius to Kelvin: K = C + 273.15
#Fahrenheit to Celsius: C = (F - 32) * 5/9
#Fahrenheit to Kelvin: K = (F + 459.67) * 5/9
#Kelvin to Celsius: C = K - 273.15
#Kelvin to Fahrenheit: F = (K * 9/5) - 459.67

print("Welcome to the Temperature Converter!")
print("Please enter a temperature value in Fahrenheit.")
temp = float(input())
Celsius = round((temp - 32) * 5/9)
Kelvin = round((temp + 459.67) * 5/9)
print("Your temperature in Celsius is " + str(Celsius) + " degrees.")
print("Your temperature in Kelvin is " + str(Kelvin) + " degrees.")
print("Thank you for using the Temperature Converter!")