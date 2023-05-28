# Slicing = create a substring by extracting elements from another string

# indexing[] or slice()
# [start:stop:step]

name = "Manny Tapia"

first_name = name[0:5:] # Can also be done as "first_name = name[:5:]" because python assumes the start of the index is the start of the string which is 0.
last_name = name[6:11:] # Can also be done as "last_name = name[6::]" becuase python assumes the end of the index is the end of the string which is 11.
funky_name = name[0:11:3] # Can also be done as "funky_name = name[::3]" becuase python assums the start of the index is the start of the string which is 0 and the end of the index is the end of the string which is 11.
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4,)

print(website1[slice])
print(website2[slice])

