''' 2️⃣ Variable Arguments: *args and **kwargs  '''

# a) *args → Variable positional arguments
# Collects extra positional arguments as a tuple.

print("\n\n ---> 1 - *args -> Variable positional arguments <------- \n")

def add_num(*args):  # collected as tuple
    print(f"args val : {args}")  # args val : (1, 4, 7)
    print(f"type of *args : {type(args)}")  # type of *args : <class 'tuple'>
    print(f"last element {args[-1]}")  # 7
    print(f"1st element {args[0]}")  # 1
    return sum(args)  # 12

print(f"Add num : {add_num(1,4,7)}")

# b) **kwargs → Variable keyword arguments
# Collects extra keyword arguments as a dictionary

print("\n\n---> 2 - **kwargs -> Variable keyword arguments <-------\n")

def print_info(**kwargs) : #  unpacking dict also it called so kwargs can be any varibale name
    print(f" **kwargs value : {kwargs}") 
    print(f"Type of kwarsg : {type(kwargs)}") # <class 'dict'>

    for key, value in kwargs.items() :
        print(f"key {key}  and value : {value}") 

       
print_info(name = "Noorul" , age = 40)


'''
Interview Tips:

    Use *args when the number of positional inputs is unknown.
    Use **kwargs for optional named arguments.
    Very handy for building flexible functions.

'''