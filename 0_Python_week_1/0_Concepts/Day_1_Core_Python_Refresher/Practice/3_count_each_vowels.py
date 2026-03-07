

# Count each vowel in a string:
# Given a string, count the number of each vowel (a, e, i, o, u) in it. The function should be case-insensitive.
'''
Write a Python function that counts the occurrence of each vowel in a given string.
The function should return a dictionary containing only the vowels that appear in the string, with the key as the vowel (in lowercase) and the value as the count.

'''
'''
Example 1:
Input: "Hello World"
Output: {'e': 1, 'o': 2}

Example 2:
Input: "Python Programming"
Output: {'o': 2, 'a': 1, 'i': 1}

Example 3:
Input: "xyz"
Output: {} (no vowels)


'''

def count_each_vowel_in_string_normal_looping (s):
    vowels= "aeiouAEIOU"
    vowels_count_dict = {}

    for c in s :
        if c in vowels:
            vowels_count_dict[c.lower()] = vowels_count_dict.get(c.lower(), 0 ) +1
        
    return vowels_count_dict



inp = "Hello World"
inp2_empty_string = " "
Input =  "xyz"
print(f"Count of each vowel in '{inp}' is: {count_each_vowel_in_string_normal_looping(inp)}") #  {'e': 1, 'o': 2}
print(f"Count of each vowel in '{inp2_empty_string}' is: {count_each_vowel_in_string_normal_looping(inp2_empty_string)}") # {} (no vowels)
print(f"Count of each vowel in '{Input}' is: {count_each_vowel_in_string_normal_looping(Input)}") # {} (no vowels)


# ✅ Variant Question (All vowels included)
'''
Write a Python function that counts the occurrence of each vowel (a, e, i, o, u) in a given string.
The function should return a dictionary containing all vowels, with the key as the vowel (in lowercase) and the value as the count.
If a vowel does not appear in the string, its count should be 0.

Example 1:
Input: "Hello World"
Output: {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}

Example 2:
Input: "Python Programming"
Output: {'a': 1, 'e': 0, 'i': 1, 'o': 2, 'u': 0}

Example 3:
Input: "xyz"
Output: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
'''

print("\n\n-----> Variant Question (All vowels included) <-----\n")

def count_each_vowel_all_vowels_included (s):
    vowels = "aeiouAEIOU"

    # initialize the dictionary with all vowels and count 0
    vowels_count_dict = {vowels.lower(): 0 for vowels in "aeiou"}

    for c in s :
        if c in vowels:
            vowels_count_dict[c.lower()] += 1
    
    return vowels_count_dict


# Perfect! Here’s the ultimate one-liner version using only str.count and dict comprehension:
def count_each_vowel_all_vowels_included_by_count_dict_comp(s):
     s = s.lower()
     d = {val: s.count(val) for val in "aeiou" }
     return d


inp = "Hello World"
inp2_empty_string = " "
Input =  "xyz"
str2 = "Python Programming apple green inbox"
print(f"Count of each vowel in '{inp}' is: {count_each_vowel_all_vowels_included(inp)}") #  {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}
print(f"Count of each vowel in '{inp2_empty_string}' is: {count_each_vowel_all_vowels_included(inp2_empty_string)}") # {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
print(f"Count of each vowel in '{Input}' is: {count_each_vowel_all_vowels_included(Input)}") # {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
print(f"Count of each vowel in '{str2}' is: {count_each_vowel_all_vowels_included(str2)}") # {'a': 1, 'e': 0, 'i': 1, 'o': 2, 'u': 0}
print(f"Count of eagc vowel in '{str2}' is count() dict comp: {count_each_vowel_all_vowels_included_by_count_dict_comp(str2)}")