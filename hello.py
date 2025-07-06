print("hello world")
# conditional operater
if 5 > 9:
    print('true')
else: 
    print('false')
# varible creation
x=10
y= 20
sum = x+y
print("sum", sum)
a = 20
a = "bhaskar"
print(a) # it will display the last value assing to that varible 

a = int(3)
a = str('bhaskarRao')
print(a)  # casting can be done using int, string and float
print(type(a))
# rules for creating a varible name 
""" 
variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""


#Many Values to Multiple Variables
a,b,c = "bhaskar","Rao", 2
print(a, b,c)
# one value to multiple varible 
a=b=c = 10
print(a,b,c)

# Unpack a Collection
    # If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking
myArray = [2,3,5]
a,b,c = myArray
print(a,b,c)

# Global Variables and local varible 
    # varible created at ourside of the function
 
myValue = 'bhaksar'

def myFun():
    myValue = "test"
    print("print my value" ,myValue)

myFun()
print(myValue)

# To create a global variable inside a function, you can use the global keyword and it can be access throught out the file 

def fun1():
    global x
    x = 2
    print('x is ', x)

fun1()
print(x)
