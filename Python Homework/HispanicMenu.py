print("Welcome to Manny's Dominican Resturant!\nHere we serve the best hispanic food in town. \nA lot of our menu items are currently on back order so bare with us for the small selection of food.")

Drinks = ["Agua", "Jugo de Chinola", "Margita", "Tequila"]
Appetizers = ["Chips con Queso", "Empanadas", "Platano Fritos"]
Entrees = ["Arroz y Abichuela con Pollo", "Platano Herbio y Salami Frito con Huevos Fritos", "Arroz Blanco con Asopao de Pollo"]
Food = [Drinks, Appetizers, Entrees]

Starting_Chocie = input("What would you like to start off with today? \n\tDrinks \n\tAppetizers \n\tEntrees \n")

if Starting_Chocie == "Drinks":
    print("Great we get you started with some drinks, at the moment we have: " + str(Food[0]))
    Customer_Choice = input("What drink would you like, 1st, 2nd, 3rd, or 4th?: ")
    if Customer_Choice == "3rd" or "4th":
        Customer_Age = int(input("By any chance can I ask for your age?: "))
        if Customer_Age >= 21:
            print("Thank you for the verification, let me grab that for you!")
        elif Customer_Age < 21:
            print("I'm sorry I won't be able to sell you alcohol since you do not meet the laws age requirment, you'll get there one day!")

if Starting_Chocie == "Appetizers":
    print("Great we get you started with some appetizers, at the moment we have: " + str(Food[1]))
if Starting_Chocie == "Entrees":
    print("Great we get you started with some entrees, at the moment we have: " + str(Food[2]))