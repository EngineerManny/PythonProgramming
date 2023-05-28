print("Ohm's Law Calculator")
print("\nThis calculator is used to aid in the creation of circuits.")

V = Voltage = int(input("\nEnter the voltage that is being supplied to the circuit: "))
Resistors = int(input("\nHow many resistors are in the circuit?: "))
ResistanceList = []
for i in range (0, Resistors):
    Resistace = int(input("Enter the resistance of resistor " + str(i + 1) + ": "))
    ResistanceList.append(Resistace)

print("\nAre these resistors in a parellel or series circuit?: ")
print("1. Parellel")
print("2. Series")
choice = int(input("Choice: "))

TotalResistance = AddedResistance = 0

if choice == 1:
    for i in range (0, Resistors):
        AddedResistance += (1 / ResistanceList[i])
    R = TotalResistance = 1 / AddedResistance
elif choice == 2:
    for i in range (0, Resistors):
        TotalResistance += (ResistanceList[i])
    R = TotalResistance

I = TotalCurrent = V / R
CurrentName = "amps"
if I < 1:
    I *= 1000
    CurrentName = "milliamps"
    P = TotalPower = (I / 1000) * V
else:
    P = TotalPower = I * V

print("\nCircuit Values:")
print("\tVoltage: " + str(V) + " volts")
print("\tResistance: " + str(R) + " ohms")
print("\tCurrent: " + str(I) + " " + CurrentName)
print("\tPower/Wattage: " + str(P) + " watts")