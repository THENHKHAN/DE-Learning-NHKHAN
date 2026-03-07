
# 9 - Nested Dictionaries
# A nested dictionary is a dictionary that contains another dictionary as a value.
# Example of a nested dictionary
'''
A nested dictionary is a dictionary that contains another dictionary (or dictionaries) as values.

This is useful to store complex data, like multiple records.
'''
# Example 1 – Student Records
nest_dict = {
    "stud1" : { "name" : "Alice" , "age" : 20 , "grade" : "A"},
    "stud2" : { "name" : "Bob" , "age" : 22 , "grade" : "B"},
    "stud3" : { "name" : "Charlie" , "age" : 21 , "grade" : "A-"}
}
print("Nested Dictionary : " , nest_dict)
# find student 2's name and grade?
stud2_name = nest_dict["stud2"]["name"]
stud2_grade = nest_dict["stud2"] ["grade"]
print(f"Student 2's name: {stud2_name} , Student 2's grade: {stud2_grade}")

'''
Notes / Interview Tips

    ==> Access nested values with multiple square brackets: dict[key1][key2]
    ==> Nested dictionaries can be arbitrarily deep
    ==> Useful for JSON-like data structures

'''


print("\n\n ###################    Dictionary Comprehension   ###############################\n ")

# 10- Dictionary Comprehension

# Dictionary comprehension lets you create dictionaries in a single line, similar to list comprehension.
# Syntax:
'''
{key_expr: value_expr for item in iterable if condition}

- key_expr: An expression that defines the key for each item in the dictionary.
- value_expr: An expression that defines the value for each item in the dictionary.
- iterable: The sequence of items to iterate over.
- condition: An optional condition that filters the items.
'''

# Example 1: Create a dictionary of squares for numbers 1 to 5
squares = {x:x**2 for x in range(1,6)}
print("Dictionary of squares from 1 to 5 : " , squares)


'''
Notes / Interview Tips

    --> Dictionary comprehension is very fast and concise
    --> Often asked in interviews: “Create a dictionary from a list with a condition”
    --> You can combine with nested loops for more advanced problems


'''# Q - find generate only even squares from 1 to 8 using dictionary comprehension
lst = [1,2,3,4,5,6,7,8]
even_numbers_squares = {num:num**2 for num in lst if num % 2 == 0 }
print("Even numbers squares from 1 to 8 using comprehension : " , even_numbers_squares)

