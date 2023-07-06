print("Hello World")
# copying examples from Lesson#1

# showig how variables are shown in the program
#name = "John"
age = 25
height = 1.67
is_student = True
has_high_degree = None

#print(name)
print(age)
print(height)
print(is_student)
print(has_high_degree)


# showing comments
    #two types of coments - short and long

fruit = "apple"

"""
really long comment that helps understand code better
"""

#Right way of naming variables
#name = "John"
age = 25
is_student = True

#Right way of using constants
PI = 3.14159
Max_Value = 100
DEFAULT_NAME = "John Doe"

#example of right way of using combining variables
width = 10
height = 5
area = width * height

"""
exampels of how not to do it 
not explaining name of variable
n = "John"
x = True
f = 10.5
using numbers or special symbols in front of variable 
2variable = "invalid"
$price = 100

using reserved word for variable
class = "invalid"
if = True

List of reserved words 
False, None, True, and, as, assert, async, await, break, class, continue, def, 
del, elif, else, except, finally, for, from, global, if, import, in, is, 
lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

"""

# Showing couple variables at the same time

x = y = z = 99
a, b, c, = 1, 2, 3

print (x, y, z, end="\t")
print (a, b, c, sep=":")

#Formats

name = "Alice"
age = 30

message = "My name is %s. I am %d years old." %(name, age)
print(message)

message = "My name is {}. I am {} years old." .format(name, age)
print(message)

message = f"My name is {name}. I am {age} years odl."
print(message)


name = "Alice"
age = "30"
message = "My name is " + name + ". I am "+ age + " years old."
print(message)

# error

message = "My name is {name}. I am {age} years odl."
print(message)

# printing emojis

print( "\N{slightly smiling face}")
print("\u263A")
print ("\U0001F600")

