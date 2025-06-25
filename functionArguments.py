


# Default Argument

def average(a = 20, b = 5):
    print("The average is ", (a + b) / 2)

average()

num1 = float(input("Enter the num 1: "))
num2 = float(input("Enter the num 2: "))

def average1(a, b):
    print("The average is ", (a + b) / 2)

average1(num1, num2)

# Keyword argument

def greet(fname, mname, lname):
    print("\n--------------------------\nHello!", fname, mname, lname, "\n--------------------------\n")

greet(fname="Narayan", mname= "Kishor", lname="Patil")



# Required Arguments

def requriedvalues(z, x = 4, y = 5):
    print(f".........{x}, {y}, {z}.........")

requriedvalues(z = 6)



# for tuple use single star
"""
def average(*numbers):
    # code
"""

# for dictionary use double stars
"""
def average2(**numbers2):
    #code
"""

def name(**name):
    print(type(name))
    print("\nHello,", name["fname"], name["mname"], name["lname"])

name(fname= "ShreeRamDootam", mname = "Sharanam", lname = "Prabadhye\n" )
