# List = used to store mulitple items in a single variable

food = ["Pizza", "Hamburger", "Hotdog", "Sphagetti", "Pudding"]

food[0] = "Sushi"

food.append("Ice Cream")
# food.remove("Hot Dog")
food.pop()
food.insert(0, "Cake")
food.sort()
# food.clear

# print(food[0])
# print(food[1])
# print(food[2])
# print(food[3])
# print(food[4])

for x in food:
    print(x)