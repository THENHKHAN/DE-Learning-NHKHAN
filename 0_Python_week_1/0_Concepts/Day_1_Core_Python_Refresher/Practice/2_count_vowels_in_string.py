
# Count vowels in a string:
# Given a string, count the number of vowels (a, e, i, o, u) in it. The function should be case-insensitive.

'''
Example: 
Input: "Hello World"
Output: 3 (vowels are 'e', 'o', 'o')
Input: "Python Programming"
Output: 4 (vowels are 'o', 'o', 'a', 'i')

'''

def count_vowels(s):
    vowels = "aeiouAEIOU" # extra space is added to avoid case sensitivity
    count = 0 
    for c in s:
        if c in vowels:
            count += 1
    return count

def count_vowels_sum(s) :
   return sum (1 for c in s if c.lower() in "aeiou" )


s = "Hello World"
print(f"Number of vowels in '{s}' is: {count_vowels(s)}")
print(f"Number of vowels in '{s}'  by sum() is: {count_vowels_sum(s)}")