'''
Tuple Data Type:

A tuple is a built-in data type in Python that is used to store multiple items in a single variable.

Tuple is an ordered collection of Python objects. 
===> The only difference between a tuple and a list is that tuples are immutable. 
        Tuples cannot be modified after it is created.
'''


print("-----> 1. Creating a Tuple <-----")

# create empty Tuple in python :
emptyTuple = ()
print("Empty Tuple : " , emptyTuple) # Empty Tuple :  ()

tup2 = (1 ,4 , "Hello" , False , 3.14)
print("Tuple with multiple data types : " , tup2) # Tuple with multiple data types :  (1, 4, 'Hello', False, 3.14)


print("Tuple with One Item")
# To create a tuple with only one item, you must add a comma after the item.
tup3  = (5)
print(f"Single item in tuple without comma : {tup3}")
print(f"Type of tup3 : {type(tup3)}") # Type of tup3 : <class 'int'>
# hence we should add a comma to create a tuple with one item
tup3_1 = (6,)
print(f"Single item in tuple with comma : {tup3_1}")
print(f"Type of tup3_1 : {type(tup3_1)}") # Type of tup3_1 : <class 'tuple'>

'''

✅ Summary

| Feature                      | List | Tuple |
| ---------------------------- | ---- | ----- |
| Mutable                      | ✔    | ❌     |
| Methods count(), index()     | ✔    | ✔     |
| append(), pop(), sort() etc. | ✔    | ❌     |
| Use Cases                     | When you need to modify the data, use a list. When you want to ensure that the data cannot be changed, use a tuple. |



'''