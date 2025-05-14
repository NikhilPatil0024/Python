print("This is a String.")
name = "Nikhil"
name2 = 'Narayan'
name3 = """This is multiline String
and can be used to write the code on the multiple lines."""
name4 = '''This is multiline string
as well. I can have the 'single' and "double" quotes things.'''

print("Hello,", name)

print("this is a string with 'quotation' and \"doubleQutoes\" ")

# that's quote escape sequence character. works with single and double.

# String functions/methods.

print("The length of the name is: ", len(name))

name3 = "Nikhil Patil 1   "
print(name3.capitalize())
print(name3.title())
print(name3.count("k")) # counts how many times the charater or an element appears.
print(name3.upper())
print(name3.lower())
print(name3.strip())
print(name3.replace(" 1", ""))
print(name3.split()) # converts the string to list. to be seperated, there should be space in between two elements or characters.
print(name3.center(155)) # will bring it to the center
print(name3.find("N")) # will return -1 if the value is not in the string.
print(name3.startswith("N"))
print(name3.endswith("l"))
# print(name3.index("ssss")) # this will throw the error if the value is not found in the string. so use the find if you don't want the error.
name3 = "NikhilPatil1" # if there are spaces then it is not alpha numeric.
print(name3.isalnum()) # will check if the string is alpha numeric or not. (comes in between/under 0-9 , A-Z and a-z ).
print(name3.isalpha()) # checks if string is written fully in alphabets or not.
name3 = "Nikhil Patil 1\n"
print(name3.isprintable()) # will check if the string is printable or not, and if there is something that will not be shown on output screen in string then it will return false.
name3 = "        "
print(name3.isspace())
name3 = "Nikhil Patil 1"
print(name3.istitle())
print(name3.isupper())
print(name3.islower())
print(name3.swapcase())

# String Slicing

print("\nString Slicing: ")

# In python the counting starts from 0(zero).
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

names = "Nikhilesh", "Shubham", "Harry", "Madhav", "Uma", "Parvati"
print(names[0:])
print(names[0:1])
print(names[4])
print(names[::2]) # will skip the one word and print the second word.
print(names[0:5:2]) # will start from zero to 5th one by skipping the every 1st element and retrun 2nd one.
print(names[0:len(names) -3]) # len is auto added to it. and this is just for example.
# lenght of names is 6
#  so 6 - 3 = 3
#  now it will count from 3 >>> Nikhilesh', 'Shubham', 'Harry'

# Quick Quiz:
nm = "Harry"
print(nm[-4: len(nm) -2 ])
# len nm 5 char = 0-4
# y = -1, r = -2, r = -3, a = -4, H = -5
# therefore, -4 = a to -2 = r 
# as there is nothing in between "a" and "r" answer is ar.

