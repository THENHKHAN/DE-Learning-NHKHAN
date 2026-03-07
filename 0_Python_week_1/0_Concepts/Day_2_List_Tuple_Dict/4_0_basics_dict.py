
# Dictionary Data Type:

# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# Dictionaries are mutable, meaning you can change their content after creation.
# ==========================================================
# PYTHON DICTIONARY – IMPORTANT TOPICS (REVISION CHECKLIST)
# ==========================================================
#
# 1. Dictionary Basics
#    - Key–value concept
#    - Rules for keys (immutable, unique)
#
# 2. Creating Dictionaries
#    - {} syntax
#    - dict() constructor
#
# 3. Accessing Values
#    - Access using key
#    - get() method
#
# 4. Adding & Updating Elements
#    - Adding new key
#    - Updating existing value
#
# 5. Deleting Elements
#    - pop()
#    - del
#
# 6. Important Dictionary Methods
#    - keys()
#    - values()
#    - items()
#    - update()
#
# 7. Looping Through Dictionary
#    - Iterate keys
#    - Iterate values
#    - Iterate key–value pairs
#
# 8. Checking Key Existence
#    - in operator
#
# 9. Nested Dictionaries
#
# 10. Dictionary Comprehension
#
# ==========================================================
# Goal: Cover the most commonly used dictionary concepts
# in Python (practical coding + interview perspective).
# ==========================================================

## ✅ Interview Tip

#*** Python dictionaries are implemented using hash tables, which makes lookup very fast (average O(1)).

'''
Key Idea

    A dictionary stores data in key → value pairs.
    Key → identifier used to access data
    Value → actual data stored
'''

# 1️⃣  Dictionary Basics : 🔑 Key concept: Key-value pairs, mutability, and rules for keys

# Example 1 : Creating a dictionary and accessing values
print("-----> 1. Creating a Dictionary and Accessing Values <-----")

student = {"name" : "Noor" , "age":25, "city": "Delhi"}
print(f"Student details as Dict : {student}") # Student details as Dict : {'name': 'Noor', 'age': 25, 'city': 'Delhi'}

# Accessing values using keys
print(f"student name : {student["name"]}") # student name : Noor
print(f"student age : {student["age"]}") # student age : 25
# print(f"student age : {student["country"]}") # KeyError: 'country' since 'country' key is not present in the dictionary
# we have a get() method to avoid KeyError when we try to access a key that is not present in the dictionary
print(f"finding country which is not in the defined dictionary using get() method : {student.get("country", "key not found")}") # key not found 
                                                                                                    # 2nd argument in get() method is default value which will be returned if key is not found in the dictionary

# adding new key-value pair to the dictionary
student["skills"]   = ["Python", "Data Analysis", "Machine Learning"]
print(f"after adding new key skills to the student dictionary : {student}") #  {'name': 'Noor', 'age': 25, 'city': 'Delhi', 'skills': ['Python', 'Data Analysis', 'Machine Learning']}

# Method 2 — Using dict() Constructor
print("\n\n-----> 2. Creating a Dictionary using dict() Constructor <-----")

# Example 2 : Creating a dictionary using dict() constructor
stud = dict(name="Guddu", age=30, city="Mumbai")
print(f"Student details as Dict using dict() constructor : {stud}") #  {'name': 'Guddu', 'age': 30, 'city': 'Mumbai'}

# Example 3 :
number = dict(one=1, two=2, three=3)
print(f"Number dictionary : {number}") # {'one': 1, 'two': 2, 'three': 3}
# data = dict() , data = {} to create empty dictionary
# {} creates an empty dictionary, not a set. this is how we can create empty set : set()

#  3️⃣. Accessing Values
print("\n\n-----> 3. Accessing Values from Dictionary <-----")

'''
You can access a dictionary value in two main ways:
 -->   Using square brackets [key] - will raise an error if the key does not exist.
 -->   Using get(key) -  returns None (or a default value) if the key does not exist.

 get() is safer: it doesn’t throw an error if the key is missing.
You can also provide a default value.


✅ Interview Tip

[] → Use when you know the key exists.
get() → Use when key might be missing.

Many interviews include questions like:
"Access a key safely without KeyError" → answer: get().
'''

#  4️⃣. Adding & Updating Elements
print("\n\n-----> 4. Adding & Updating Elements in Dictionary <-----\n")

'''
Key Idea

--> Adding a new key–value pair → simply assign a value to a new key.
--> Updating an existing key → assign a new value to an existing key.

'''
info = {"name":"Alice", "age": 28}
print(f"Original Dictionary : {info}") #  {'name': 'Alice', 'age': 28}
# Adding a new key-value pair
info["city"] = "new york"
print(f"After adding new key city : {info}") # {'name': 'Alice', 'age': 28, 'city': 'new york'}
# Updating an existing key
info["age"] = 50
print(f"After updating age to 50 : {info}") # {'name': 'Alice', 'age': 50, 'city': 'new york'}

'''
Notes / Interview Tips

--> You don't need a special method to add/update; assignment works for both.
--> update() method can also be used (will cover in the methods section).
--> Adding multiple keys at once can be done with update().

'''
#  5️⃣. Deleting Elements
print("\n\n-----> 5. Deleting Elements from Dictionary <-----\n")

'''
Python provides multiple ways to remove items from a dictionary:

    -->pop(key) → removes a specific key and returns its value. Raises KeyError if key is not found. But if we provide a default value (pop(key, default)) as a second argument, it will return that instead of raising an error. called safe deletion.
    -->del → removes a key (or the entire dictionary). Raises KeyError if key is not found.
    -->clear() → removes all items from the dictionary. Raises KeyError if key is not found.
'''
myDict = {"name": "Bob", "age": 35, "city": "Chicago"}
print(f"Original Dictionary : {myDict}") # {'name': 'Bob', 'age': 35, 'city': 'Chicago'}
# Using pop() to remove a key
removed_age_value = myDict.pop("age") # pop() removes the key "age" and returns its value (35)
print(f"Value of removed key 'age': {removed_age_value}") # Value of removed key 'age': 35
print(f"After popping age : {myDict}") # {'name': 'Bob', 'city': 'Chicago'}

# Using del to remove a key
del myDict["city"] # del removes the key "city" from the dictionary. And it does not return the value of the removed key.
print(f"After deleting city using del : {myDict}") # {'name': 'Bob'}

# Optional – Remove All Items: clear() method removes all items from the dictionary, leaving it empty.
myDict.clear() # clear() removes all items from the dictionary, leaving it empty.
print(f"After clearing the dictionary using clear() method : {myDict}") # After clearing the dictionary using clear() method : {}

'''
✅ Interview Tip

--> pop() → use when you need the removed value.
--> del → use for simple deletion.
--> clear() → use to empty the dictionary.

'''

#  6️⃣. Important Dictionary Methods
print("\n\n-----> 6. Important Dictionary Methods <-----\n")
'''
6. Important Dictionary Methods

    --> We'll cover 4 key methods:
    --> keys() → returns all keys
    --> values() → returns all values
    --> items() → returns key-value pairs
    --> update() → adds or updates multiple key-value pairs
'''

dict1 = {"name": "Charlie", "age": 40, "city": "San Francisco"}
print(f"Original Dictionary : {dict1}") # {'name': 'Charlie', 'age': 40, 'city': 'San Francisco'}

# 1- keys() method returns a view object that displays a list of all the keys in the dictionary.

print("\n\n### Using keys() method to get all keys in the dictionary ###\n")

allKeysOfDict = dict1.keys() # keys() method returns a view object that displays a list of all the keys in the dictionary.
print(f"All keys in the dictionary : {allKeysOfDict}") # All keys in the dictionary : dict_keys(['name', 'age', 'city'])

# then we can use loop to iterate through the keys
print("Iterating through keys using keys() method : ")
i = 0 
for key in allKeysOfDict:
    print(f"key_{i} : {key}")
    i += 1

# 2- values() method returns a view object that displays a list of all the values in the dictionary.

print("\n\n### Using values() method to get all values in the dictionary ###\n")

allValuesOfDict = dict1.values() # values() method returns a view object that displays a list of all the values in the dictionary.
print(f"All values in the dictionary : {allValuesOfDict}") # All values in the dictionary : dict_values(['Charlie', 40, 'San Francisco'])


# 3- items() method returns a view object that displays a list of dictionary's key-value tuple pairs.

print("\n\n### Using items() method to get all key-value pairs in the dictionary ###\n")

allItemsOfDictOrKeyValuePairs = dict1.items() # items() method returns a view object that displays a list of dictionary's key-value tuple pairs.
print(f"All key-value pairs in the dictionary : {allItemsOfDictOrKeyValuePairs}") # All key-value pairs in the dictionary : dict_items([('name', 'Charlie'), ('age', 40), ('city', 'San Francisco')])
# lets iterate through the key-value pairs using loop:
print("Lets print using loop to iterate through key-value pairs : ")
for key, value in allItemsOfDictOrKeyValuePairs:
    # print(f"key : {key} , value : {value}")
    # or 
    print(f"{key} -->  {value}")

# 4️- update() : The update() method is used to add or update multiple key-value pairs in a dictionary at once. It takes another dictionary (or an iterable of key-value pairs) as an argument and updates the original dictionary with the new key-value pairs.

print("\n\n### Using update() method to add or update multiple key-value pairs in the dictionary ###\n")
dict2 = {"name": "David", "age": 45, "country": "USA"}
print(f"Original Dictionary : {dict2}") # Original Dictionary : {'name': 'David', 'age': 45, 'country': 'USA'}
# Using update() to add a new key-value pair and update existing key-value pair
# Example 2 – Update Existing Key
tempDict = {"city" : "Los Angeles"}
dict2.update(tempDict) # update() method adds the key-value pair from tempDict to dict2
print(f"After updating dict2 with tempDict using update() method : {dict2}") # After updating dict2 with tempDict using update() method : {'name': 'David', 'age': 45, 'country': 'USA', 'city': 'Los Angeles'}

#NOTE-  We can also update multiple key-value pairs at once using update() method

# Example 2 – Update Existing Key 
tempDict2 = {"name" : "David Beckham", "age": 50}
print(f"Original Dictionary : {dict2}") # Original Dictionary : {'name': 'David', 'age': 45, 'country': 'USA', 'city': 'Los Angeles'}
dict2.update(tempDict2) # update() method updates the existing key-value pairs in dict2 with the key-value pairs from tempDict2
print(f"After updating dict2 with tempDict2 using update() method : {dict2}") # After updating dict2 with tempDict2 using update() method : {'name': 'David Beckham', 'age': 50, 'country': 'USA', 'city': 'Los Angeles'}


'''
✅ Interview Tips

    --> keys(), values(), items() → often used in loops.
    --> update() → frequently used for merging dictionaries.

'''

# 7️⃣ Using Tuples to Create a Dictionary

# Python’s dict() can take an iterable of tuples, where each tuple is (key, value).

print("\n\n-----> 7. Using Tuples to Create a Dictionary <-----\n")
# Example 1 : Creating a dictionary from a list of tuples
listOfTuples = [("name", "Noorul") , ("age" , 33) , ("city" , "Delhi")] # ✅ Each tuple is (key, value)

print(f"List of tuples : {listOfTuples}") # List of tuples : [('name', 'Noorul'), ('age', 33), ('city', 'Delhi')]
# using Dict() constructor to create a dictionary from list of tuples
dictFromListOfTuples = dict(listOfTuples) # dict() constructor can take an iterable of tuples, where each tuple is (key, value).
print(f"Dictionary created from list of tuples : {dictFromListOfTuples}") # Dictionary created from list of tuples : {'name': 'Noorul', 'age': 33, 'city': 'Delhi'}

'''

✅ Interview Tip
--> dict() can take a list of tuples to create a dictionary.
--> Each tuple should be in the form (key, value).
--> This is a common way to create dictionaries from data that is naturally represented as pairs.
--> Example: converting a list of (key, value) pairs into a dictionary.

Notes / Interview Tips

==> This is frequently asked: “Convert list of tuples into a dictionary”.
==> Works with any iterable of (key, value), like list, tuple, set (of tuples).
==> Keys still must be immutable (str, int, tuple).
==> Values can be of any type.
==> If there are duplicate keys in the list of tuples, the last occurrence will overwrite previous ones.
==> Example: dict([("a", 1), ("b", 2), ("a", 3)]) → {'a': 3, 'b': 2} (last "a" overwrites the first one).
==> This method is very useful when you have data in the form of pairs and want to quickly convert it into a dictionary for easy access.
==> Common in scenarios like reading CSV data, processing API responses, etc.
==> Always ensure that the keys in the tuples are of an immutable type, otherwise you will get a TypeError when trying to create the dictionary.
==> Example of error: dict([(["listKey"], "value")]) → TypeError: unhashable type: 'list' because list is mutable and cannot be used as a key in a dictionary.
==> Example of valid keys: dict([("tupleKey", "value")]) → {'tupleKey': 'value'} because tuple is immutable and can be used as a key in a dictionary.
==> This is a common technique in data processing and is often used in interviews to test understanding of both tuples and dictionaries.
===> Always remember that the keys must be immutable and unique for the dictionary to work properly.
===> If you have duplicate keys in the list of tuples, the last occurrence will overwrite previous ones, so be cautious when creating dictionaries from lists of tuples with potential duplicates.
==> Example of duplicate keys: dict([("a", 1), ("b", 2), ("a", 3)]) → {'a': 3, 'b': 2} (last "a" overwrites the first one).
===> This method is very useful when you have data in the form of pairs and want to quickly convert it into a dictionary for easy access.
===> Common in scenarios like reading CSV data, processing API responses, etc.
===> Always ensure that the keys in the tuples are of an immutable type, otherwise you will get a TypeError when trying to create the dictionary.
==> Example of error: dict([(["listKey"], "value")]) → TypeError: unhashable type: 'list' because list is mutable and cannot be used as a key in a dictionary.
==> Example of valid keys: dict([("tupleKey", "value")]) → {'tupleKey': 'value'} because tuple is immutable and can be used as a key in a dictionary.

'''


# next 9-10 topics will be covered in the next file : 4_1_nested_dictComprehension_dict.py.py