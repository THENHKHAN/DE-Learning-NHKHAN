
# Will do 7 most asked dictionary programs in Python:

# 1️⃣ Count Frequency of Items : 🔑 Key concepts: get() + adding/updating keys

# Problem: Count how many times each element appears in a list.

print("\n\nProblem-1: Count how many times each element appears in a list.???????????????\n")

nums = [1, 2, 2, 3, 1, 2]
print("Input List:", nums)
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1 # Using get() to handle missing keys and increment count since if didn't exist it will return 0 and then we add 1 to it.
print("Frequency of Items:", freq)


# 2️⃣ Merge Two Dictionaries: 🔑 Key concept: update() Or unpacking operator (**)
# Problem: Combine two dictionaries; if keys overlap, update values.

print("\n\nProblem-2: Merge Two Dictionaries.???????????????\n")
dict1 = dict(a= 1, b=2 , c = 4 ) # though dict() constructor.
dict2 = {'name' : 'Alice', 'age' : 30} # using literal syntax.
print(f"Dict1: {dict1} and Dict2: {dict2}")

# lets use update() method to merger dict1 and dict2 : Here we dont have to create a new dictionary, we can directly update dict1 with the key-value pairs from dict2.
dict1.update(dict2) # this will update dict1 with the key-value pairs from dict2. If there are any overlapping keys, the values from dict2 will overwrite those in dict1.
print("Merged Dictionary using update():", dict1)   

# Merging using unpacking operator: Here we create a new dictionary by unpacking both dict1 and dict2. This method is more concise and creates a new dictionary without modifying the original ones.
merged_dict = {**dict1, **dict2} # This will create a new dictionary by unpacking both dict1 and dict2. If there are overlapping keys, the values from dict2 will overwrite those from dict1.
print("Merged Dictionary using unpacking operator:", merged_dict)


# 3️⃣ Find Keys by Value : 🔑 Key concept: keys() + condtion OR items() + list comprehension
# Problem: Find all keys in a dictionary that have a certain value.

print("\n\nProblem-3: Find all keys in a dictionary that have a certain value.???????????????\n")
scores = {"Alice": 90, "Bob": 80, "Charlie": 90, "David": 70, "Eve": 80, "Frank": 90}
target_value = 90
# So here what we have to do is to find all the keys that have the value 90. We can do this by iterating through the dictionary and checking for the value.

# Method 1: Using keys() and condition:
list_of_key_of_dict = scores.keys() # this will give us a view of all the keys in the dictionary.
print("Keys in the dictionary:", list_of_key_of_dict)
matching_keys_list = []
for key in list_of_key_of_dict:
    if scores[key] == target_value :
        matching_keys_list.append(key)
print(f"Keys with value {target_value} using keys() and condition:", matching_keys_list)

#  Method 2: Using items() and list comprehension:
# matching_keys_list_list_comprehension = [key for key in scores.keys() if scores[key] == target_value] # this will create a list of keys for which the value in the scores dictionary is equal to the target_value.
matching_keys_list_list_comprehension = [key for key, value in scores.items() if value == target_value] # this will create a list of keys for which the value in the scores dictionary is equal to the target_value.
print(f"Keys with value {target_value} using items() and list comprehension:", matching_keys_list_list_comprehension)


# 4️⃣ Nested Dictionary Access : 🔑 Key concept: Nested dictionaries
# Problem: Access a specific value in nested dictionaries.

print("\n\nProblem-4: Access a specific value in nested dictionaries.???????????????\n")
nested_stud_dict = { 
    'class_a' : {'name': 'Noorul', 'marks': 80},
    'class_b' : {'name': 'Alice', 'marks': 70},
    'class_c' : {'name':'Eve', 'marks' : 67}
}
# find the class_b student name and class_c marks
class_b_name = nested_stud_dict['class_b']['name']
class_c_marks = nested_stud_dict['class_c']['marks']
print(f"Class B student name: {class_b_name}")
print(f"Class C student marks: {class_c_marks}")


# 5️⃣ Dictionary Comprehension for Transformation: 🔑 Key concept: Dictionary comprehension Or normal for loop.
# Problem: Convert a list into a dictionary with some rule. 
# Rule - Find the square of all odd numbers in the given list.

print("\n\nProblem-5: Convert a list into a dictionary with some rule.???????????????\n")

numbers = [1,2,3,4,5,6,7,8,9,10]
# method 1: using normal for loop:
squared_odd_dict = {}
for num in numbers:
    if num%2 != 0 :
        squared_odd_dict[num] = num*num # or we can use num**2 to find the square of the number.
print("Squared odd numbers using normal for loop:", squared_odd_dict)

# Method 2: using dictionary comprehension:
squared_odd_dict_comp = {num:num**2 for num in numbers if  num % 2 != 0} # this will create a dictionary where the keys are the odd numbers from the list and the values are their squares.
print("Squared odd numbers using dictionary comprehension:", squared_odd_dict_comp)

# 6️⃣ Remove Key Safely: 🔑 Key concept: pop(key, default)
# Problem: Remove a key from a dictionary without causing an error if the key doesn't exist.
# Problem: Delete a key if it exists without raising KeyError.
print("\n\nProblem-6: Remove a key from a dictionary without causing an error if the key doesn't exist.???????????????\n")

my_dict = dict(a=33, b=99, c=55, d=77)
key_to_remove = 'b'
deleted_element1 = my_dict.pop(key_to_remove, None) 
deleted_element2 = my_dict.pop('p', "Key not found in dictionary") # this will return "Key not found in dictionary" instead of raising KeyError since 'p' is not present in the dictionary.
print(f"Deleted element for key '{key_to_remove}':", deleted_element1) # 99
print(f"Deleted element for key 'p' (not present):", deleted_element2) # "Key not found in dictionary"
print("Dictionary after deletion:", my_dict)




# 7️⃣ Sort Dictionary by Value : 🔑 Key concept: Sorting a dictionary by values using normal for loop and condition without using any in-built function and lambda function.
# Problem: Sort a dictionary based on its values.
print("\n\nProblem-7: Sort a dictionary based on its values.???????????????\n")
my_dict = dict(a=33, b=99, c=55, d=77)
print("Original Dictionary:", my_dict)
# Sorting the dictionary by values:

# Method 1: Using normal for loop and condition only without using any in-built function and lambda function:

'''
How it works

Compare adjacent elements
Largest values bubble to the end

[90,80,85]

Pass1 → biggest goes last
Pass2 → second biggest placed

Time Complexity:
O(n²)

This pattern is used often in:

    ==> Selection sort
    ==> Minimum / maximum search
    ==> Pair comparisons
'''

# Step 1: Convert dictionary to list of tuples
list_of_tuples_of_key_value_pairs = list(my_dict.items()) # this will give us a list of tuples where each tuple is (key, value).
print(f"List of tuples of key-value pairs: {list_of_tuples_of_key_value_pairs}") # [('a', 33), ('b', 99), ('c', 55), ('d', 77)]
# now will access the values of each tuple and compare them and sort them. NOTE- You'll understand more if have already done a sorting in list of numbers using normal for loop and condition.
# if the is done then we just convert list of tuples back to dictionary using dict() constructor.

# sorting the list of tuples based on the value. # Step 2: Bubble sort based on value

for i in range(len(list_of_tuples_of_key_value_pairs)): # run total number of tuples.
    # this loop below loop will run for each tuple and compare the value of that tuple with the value of all the other tuples and sort them based on the value.
    for j in range(i+1, len(list_of_tuples_of_key_value_pairs)): # run for the remaining tuples after the current tuple.
        if list_of_tuples_of_key_value_pairs[i][1] > list_of_tuples_of_key_value_pairs[j][1]: # compare the value of the current tuple with the value of the next tuple.
           # then swap the tuples if the value of the current tuple is greater than the value of the next tuple.
           list_of_tuples_of_key_value_pairs[i], list_of_tuples_of_key_value_pairs[j] = list_of_tuples_of_key_value_pairs[j], list_of_tuples_of_key_value_pairs[i] # this will swap the tuples if the value of the current tuple is greater than the value of the next tuple.

# Step 3: Convert back to dictionary

# now we have the sorted list of tuples based on the value, we just need to convert it back to dictionary.
sorted_dict = dict(list_of_tuples_of_key_value_pairs) # this will convert the sorted list of tuples back to dictionary.
print("(by dict() constructor - Sorted Dictionary by values using normal for loop and condition:", sorted_dict)

sorted_dict_loop = {}  # let create an empty dictionary to store the sorted key-value pairs.
for key, value in list_of_tuples_of_key_value_pairs:
    sorted_dict_loop[key] = value
print("Storing Sorted list of tuples to Dictionary by key-values pairs using normal for loop  (alternative way):", sorted_dict_loop)

# ✅ Good for DSA interviews because it shows sorting logic.
'''
Key Idea

    --> Convert dictionary → list of (key, value) tuples
    --> Apply manual sorting using loops
    --> Rebuild dictionary from sorted list

Why interviews sometimes ask this

    --> They want to see if you understand:
    --> dictionary structure
    --> tuple indexing (items[j][1])
    --> manual sorting logic


'''

# 2️⃣ Method 2 — Using sorted() (Most Common in Python) : 
# will use sorted() function to sort the list of tuple based on the value and then convert it back to dictionary using dict() constructor.
my_dict2 = dict(a=33, b=99, c=55, d=77)
print("Original Dictionary:", my_dict2)
sorted_dict_sorted  = sorted(my_dict2.items(), key = lambda item: item[1]) # this will sort the list of tuples based on the value (item[1]) and return a new sorted list of tuples.
 # [('a', 33), ('c', 55), ('d', 77), ('b', 99)]
print("METHOD 2 - Sorted list of tuples based on value using sorted() and lambda function:", dict(sorted_dict_sorted)) # this will convert the sorted list of tuples back to dictionary.
# {'a': 33, 'c': 55, 'd': 77, 'b': 99}

# if you want to sort in descending order then you can use reverse=True in the sorted() function like this: thne we put an extra argument reverse=True in the sorted() function like this:
# sorted_dict_sorted_descending  = sorted(my_dict2.items(), key = lambda item: item[1], reverse=True) # this will sort the list of tuples based on the value (item[1]) in descending order and return a new sorted list of tuples.
# [('b', 99), ('d', 77), ('c', 55), ('a', 33)]



# 8️⃣ Unpacking Dictionaries: BONUS: 🔑 Key concept: Unpacking operator (**)
# Problem: Merge two dictionaries using unpacking operator.
print("\n\nProblem-8: Merge two dictionaries using unpacking operator.???????????????\n")
dict_a = {'x': 10, 'y': 20}
dict_b = {'y': 30, 'z': 40}
# Merging using unpacking operator:
merged_dict_unpacking = {**dict_a, **dict_b} # This will create a new dictionary by unpacking both dict_a and dict_b. If there are overlapping keys, the values from dict_b will overwrite those from dict_a.
print("Merged Dictionary using unpacking operator:", merged_dict_unpacking)

# Note: The unpacking operator (**) can also be used to create a new dictionary by combining an existing dictionary with new key-value pairs. For example:
d = {'a': 1, 'b': 2, 'c': 3}
unp = {**d, 'f' : 55} # This will create a new dictionary that contains all the key-value pairs from d, plus a new key 'f' with the value 55.
print("New dictionary using unpacking operator with additional key-value pair:", unp)   


# 