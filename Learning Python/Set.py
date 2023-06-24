# set = a collection which is unordered, unindexed. No duplicate values

utensils = {"Fork", "Spoon", "Knife"}
dishes = {"Bowl", "Plate", "Cup"}

utensils.add("Napkin")
utensils.remove("Fork")
#utensils.clear()
utensils.update(dishes)
dishes.update(utensils)
dinner_table = utensils.union(dishes)
dinner_table = dishes.union(utensils)

for x in utensils:
    print(x)

for x in dishes:
    print(x)

for x in dinner_table:
    print(x)

print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))
print(dishes.intersection(utensils))