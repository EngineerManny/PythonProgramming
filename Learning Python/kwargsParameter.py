# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a funcntion can accept a varying amount of keywoard arguments

# an example of a program that will accept only 2 keyword arguments becuase it has 2 parameters
#def Hello(first, last):
   # print("Hello " + first + " " + last)

#Hello(first = "Manny", last = "Tapia")

def Hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs ['last'])
    print("Hello",end =" ")
    for key,value in kwargs.items():
        print(value, end=" ")

Hello(title = "Dr.", first = "Manuel", middle = "Alberto", last = "Tapia Jr Arredondo")