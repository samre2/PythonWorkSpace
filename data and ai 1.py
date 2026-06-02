
#introduction to python programming
print("hello word")

#input function
person  = input("What is you name?")
age = input("What is your age?")

#printing the values of person and age
print(person)
print(age)

#if statement
a = 7
if (a > 5):
    print("a is greater than 5")


#Formatted string
print(f"person_name is {person} and person_age is {age}")

#variables and data types

name = "Alice"
print(name)

name2 = "Bob"
age2 = 30
address = "123 Main St"

print(f"name2 is {name2}, age2 is {age2}, and address is {address}")

#rules defining variables
#1. Variable names must start with a letter or an underscore
#2. Variable names can only contain letters, numbers, and underscores
#3. Variable names are case-sensitive
#4. Variable names cannot be a reserved keyword in Python

#swapping values of two variables
a =10
b  = 6
print(f"Before swapping: a = {a}, b = {b}")
print(f"After Swapping: a = {b}, b = {a}")
print(a)
print(b)

#deleting a variable
a =24
print(a)
del a
print(f"b is {b}")

#operators in python
#1. Arithmetic operators    + - * / % ** //

aa = 5
bb = 2
print(f"addition of aa and bb is {aa + bb}" )  # Addition
print(f"subtraction of aa and bb is {aa - bb}" )  # Subtraction   
print(f"multiplication of aa and bb is {aa * bb}" )  # Multiplication
print(f"division of aa and bb is {aa / bb}" )  # Division
print(f"modulus of aa and bb is {aa % bb}" )  # Modulus
print(f"exponentiation of aa and bb is {aa ** bb}" ) # Exponentiation
print(f"floor division of aa and bb is {aa // bb}" ) # Floor division

#2. Comparison operators     == != > < >= <=    
x = 10
y = 5

print(f"x is equal to y: {x == y}")  # Equal to
print(f"x is not equal to y: {x != y}")  # Not equal to 
print(f"x is greater than y: {x > y}")  # Greater than
print(f"x is less than y: {x < y}")  # Less than
print(f"x is greater than or equal to y: {x >= y}")  # Greater than or equal to
print(f"x is less than or equal to y: {x <= y}")  # Less than or equal to
# 
#      
#3. Logical operators        and, or, not   
a1 = True
b2 = False
print(f"a1 and b2 is {a1 and b2}")  # Logical AND
print(f"a1 or b2 is {a1 or b2}")  # Logical OR
print(f"not a1 is {not a1}")  # Logical NOT

a1= 7
b1 = 3
if (a1 > 5 and b1 < 5):
    print("a1 is greater than 5 and b1 is less than 5")




#4. Assignment operators     = += -= *= /= %= **= //=   
a = 10
a += 5  # Equivalent to a = a + 5
print(f"After addition assignment, a is {a}")
a -= 3  # Equivalent to a = a - 3
print(f"After subtraction assignment, a is {a}")
a *= 2  # Equivalent to a = a * 2
print(f"After multiplication assignment, a is {a}")
a /= 4  # Equivalent to a = a / 4
print(f"After division assignment, a is {a}")
a %= 3  # Equivalent to a = a % 3
print(f"After modulus assignment, a is {a}")

#5. Bitwise operators        & | ^ ~ << >>
#Note: Bitwise operators work on the binary representation of integers.
#For example, the number 5 is represented in binary as 0101, and the number 3 is represented as 0011. The bitwise operators will perform operations on each corresponding bit of the numbers.
    
x = 5  # In binary: 0101
y = 3  # In binary: 0011
print(f"x & y is {x & y}")  # Bitwise AND
print(f"x | y is {x | y}")  # Bitwise OR
print(f"x ^ y is {x ^ y}")  # Bitwise XOR
print(f"~x is {~x}")  # Bitwise NOT
print(f"x << 1 is {x << 1}")  # Left shift
print(f"x >> 1 is {x >> 1}")  # Right shift 

#membership operators     in, not in
my_list = [1, 2, 3, 4, 5]
print(f"2 is in my_list: {2 in my_list}")  # True
print(f"6 is not in my_list: {6 not in my_list}")  # True

#hexadecimal numbers
hex_num = 0x1A  # Hexadecimal representation of 26
print(f"The hexadecimal number 0x1A is equal to {hex_num} in decimal.")



#classification of data types

#1. Numeric types: int, float, complex
num1 = 10  # Integer
num2 = 3.14  # Float
num3 = 2 + 3j  # Complex number
print(f"num1 is {num1}, num2 is {num2}, and num3 is {num3}")

#2. Sequence types: list, tuple, range

my_list = [1, 2, 3, 4, 5]  # List
my_tuple = (1, 2, 3, 4, 5)  # Tuple
my_range = range(1, 10)  # Range
print(f"My list is: {my_list}")
print(f"My tuple is: {my_tuple}")
print(f"My range is: {list(my_range)}")

#3. Text type: str

my_string = "Hello, World!"  # String
print(f"My string is: {my_string}")
#4. Mapping type: dict
my_dict = {"name": "Alice", "age": 30, "city": "New York"}  # Dictionary
print(f"My dictionary is: {my_dict}")


#set types: set, frozenset
my_set = {1, 2, 3, 4, 5}  # Set
my_frozenset = frozenset([1, 2, 3, 4, 5])  # Frozenset
print(f"My set is: {my_set}")
print(f"My frozenset is: {my_frozenset}")

#unordered collection of unique elements
my_set = {1, 2, 3, 4, 5}
print(f"My set is: {my_set}")
my_set.add(6)  # Adding an element to the set
print(f"After adding 6, my set is: {my_set}")
my_set.remove(3)  # Removing an element from the set
print(f"After removing 3, my set is: {my_set}")

