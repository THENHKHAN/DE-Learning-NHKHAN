#  1️⃣ Variables

name  = "Noorul"
age = 26
print(f"Name :  {name}")
print(f"Age: {age}")
# float 
number = 3.14
print(f"Float number: {number}")

# 2️⃣ Data Types
print(f"Type of name : {type(name)}")
print(f"Type of age : {type(age)}")
print(f"Type of number : {type(number)}")


print(" ----- Boolean type --------")
print(f"Is 5 is greater than 3 ? : {5>3}")
print(f"Is 5 is greater than 10 ? : {5>10}")

print(" ----- Data type --------")

print(f"Type check of age - {type(age)== int}")
print(f"Type check of name - {type(name)== str}")
print(f"Type check of number - {type(number)== float}")
print(f"Type check of name - {type(name)== int}")


print("--- Type conversion ---  ")
print(f"Number from float to Int :  {int(number)} and type is {type(int(number))}")

# Simliarly we can convert from int to float and str to int and so on. Just by using the type name as a function and passing the value to be converted as an argument.
'''

Name :  Noorul
Age: 26
Float number: 3.14
Type of name : <class 'str'>
Type of age : <class 'int'>
Type of number : <class 'float'>
 ----- Boolean type --------
Is 5 is greater than 3 ? : True
Is 5 is greater than 10 ? : False
 ----- Data type --------
Type check of age - True
Type check of name - True
Type check of number - True
Type check of name - False

print("--- Type conversion ---  ")
Number from float to Int :  3 and type is <class 'int'>

'''