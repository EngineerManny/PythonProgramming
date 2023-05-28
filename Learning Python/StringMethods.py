name = "Manny"
lowercasename = "manny"
uppercasename = "MANNY"
birthdate = 2

print(len(name)) #len() counts how many characters are in the string.
print(name.find("M")) #find(M) finds the index of the letter M in the string.
print(name.find("a")) #find(a) finds the index of the letter a in the string.
print(name.find("n")) #find(n) finds the index of the letter n in the string.
print(name.find("n")) #find(n) finds the index of the letter n in the string.
print(name.find("y")) #find(y) finds the index of the letter y in the string.

print(lowercasename.capitalize()) #capalize() makes the first letter of the string uppercase.
print(lowercasename.upper()) #upper() makes all the letters in the string uppercase.
print(uppercasename.lower()) #lower() makes all the letters in the string lowercase.
print(name.isdigit()) #isdigit() checks if the string is only digits.
print(str(birthdate).isdigit()) #isdigit() checks if the string is only digits.
print(name.isalpha()) #isalpha() checks if the string is only alphabetical letters.
print(name.count("M")) #count(M) counts how many M's times the string is in the string.
print(name.count("a")) #count(a) counts how many n's times the string is in the string.
print(name.count("n")) #count(n) counts how many n's times the string is in the string.
print(name.count("y")) #count(y) counts how many y's times the string is in the string.

print(name.replace("Manny", "Manny Tapia")) #replace(Manny, Manny Tapia) replaces the first string with the second string.
print(name*3) #multiplies the string by the number.