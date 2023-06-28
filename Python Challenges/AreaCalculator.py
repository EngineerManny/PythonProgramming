import math

def area_of_tetrahedron(edge):
    return math.pow(int(edge),2) * math.sqrt(3)

def area_of_circle(radius):
    return math.pow(int(radius),2) * math.pi

def area_of_triangle(base, height):
    return (1/2) * (int(base)) * (int(height))

print("This calculator will use the dimensions of different shapes to calculate the area of said shapes.\n\t1. Tetrahedron\n\t2. Circle \n\t3. Triangle")

shape_of_choice = int(input("What shape would you like to find the area of?: "))

if shape_of_choice == 1:
    edge = float(input("What is the measurment of a side of the tetrahedron?: "))
    print("The area of the tetrahedron is", str(round(area_of_tetrahedron(edge))) + ".")

if shape_of_choice == 2:
    radius = float(input("What is the radius of the circle?: "))
    print("The area of the circle is", str(round(area_of_circle(radius))) + ".")

if shape_of_choice == 3:
    base = float(input("What is the base of the triangle?: "))
    height = float(input("What is the height of the triangle?: "))
    print("The area of the triangle is", str(round(area_of_triangle(base, height))) + ".")