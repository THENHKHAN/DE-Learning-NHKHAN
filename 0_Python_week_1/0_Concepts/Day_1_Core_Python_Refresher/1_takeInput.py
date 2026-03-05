# print("What's you name ?" , sep= "#" , end= " ")
# name = input("What's you name ? " )
# print(f"hello {name} !")

val = input("Enter your value: ")
print(f"Hello : {val}")

print("-- Taking Multiple Inputs --")
a, b = input("Enter two numbers separated by space: ").split()
print(f"First number: {a}")
print(f"Second number: {b}")


n1, n2 = input("Enter two String separated by space: ").split()
print(f"First Name: {n1}")
print(f"Second Name: {n2}")


'''

$ python 0_Python_week_1/0_Concepts/Day_1_Core_Python_Refresher/1_takeInput.py
Enter your value: Noorul
Hello : Noorul
-- Taking Multiple Inputs --
Enter two numbers separated by space: 3 10
First number: 3
Second number: 10
Enter two String separated by space: Noorul Khan
First Name: Noorul
Second Name: Khan

'''