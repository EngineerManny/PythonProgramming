# Loop Control Statements = change a loops execution from it's normal sequence

# break = used to terminate the loop entirely
# contiue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter you name: ")
    if name != "":
        break

phone_number = "609-892-9642"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(0,21):

    if i == 13:
        pass
    else:
        print(i)