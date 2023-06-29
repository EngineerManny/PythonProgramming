import math

def area_of_tetrahedron(edge):
    return math.pow(int(edge),2) * math.sqrt(3)

def area_of_circle(radius):
    return math.pow(int(radius),2) * math.pi

def area_of_triangle(base, height):
    return (1/2) * (int(base)) * (int(height))

def valueError():
    print("Invalid input please enter a valid numeric value.")

print("This calculator will use the dimensions of different shapes to calculate the area of said shapes.\n\t1. Tetrahedron\n\t2. Circle \n\t3. Triangle")

shape_of_choice = int(input("What shape would you like to find the area of?: "))

while shape_of_choice != 1 and shape_of_choice != 2 and shape_of_choice != 3:
    valueError()
    shape_of_choice = int(input("What shape would you like to find the area of?: "))
else:
    if shape_of_choice == 1:
        edge = float(input("What is the measurment of a side of the tetrahedron?: "))
        while edge <= 0:
            valueError()
            edge = float(input("What is the measurment of a side of the tetrahedron?: "))
        else:
            print("The area of the tetrahedron is {:.2f}".format(area_of_tetrahedron(edge)) + ".")
    elif shape_of_choice == 2:
        radius = float(input("What is the radius of the circle?: "))
        while radius <= 0:
            valueError()
            radius = float(input("What is the radius of the circle?: "))
        else:
            print("The area of the circle is {:.2f}".format(area_of_circle(radius)) + ".")
    elif shape_of_choice == 3:
        base = float(input("What is the base of the triangle?: "))
        height = float(input("What is the height of the triangle?: "))
        while base <= 0 or height <= 0:
            valueError()
            base = float(input("What is the base of the triangle?: "))
            height = float(input("What is the height of the triangle?: "))
        else:
            print("The area of the triangle is {:.2f}".format(area_of_triangle(base, height)) + ".")
    else:
        valueError()