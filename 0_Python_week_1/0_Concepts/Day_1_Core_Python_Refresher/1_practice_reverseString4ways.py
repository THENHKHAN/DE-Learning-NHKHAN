'''
❓ Is it possible to reverse a string in-place in Python?
❌ No — it is NOT possible.

Because strings are immutable in Python, you cannot modify them in-place.

text = "Python"
text[0] = "p"   # ❌ Error

TypeError: 'str' object does not support item assignment

So reversing in-place is impossible.

===> No, strings cannot be reversed in-place in Python because they are immutable. You must create a new string or convert it to a list first.

'''

# Reverse a string

myStr = "abc"
# exected output: "cba"

# Solution 1: Using slicing
revStr = myStr[ : : -1 ]
print(f"Slicing :  {revStr}" ) # Slicing :  cba

'''
---> ⏱ Time Complexity: O(n)

Python visits each character once.

---> 💾 Space Complexity: O(n)

A new string of size n is created.

Strings are immutable → cannot reuse memory.

✔ Time: O(n)
✔ Space: O(n)
✔ Clean and fast
'''

# reversed() + join()

revStr2 = "".join(reversed(myStr))
print(f"Using reversed() + join() : {revStr2}") # Using reversed() + join() : cba

'''
---> ⏱ Time Complexity: O(n)

reversed() iterates through all characters.

join() builds a new string.

---> 💾 Space Complexity: O(n)

New string is created.
Strings are immutable → cannot reuse memory.
'''


# Solution 3: Using for loop
strholder = ""
for char in myStr:
    strholder = char + strholder # a + '' => a , b + a => ba , c + ba => cba

print(f"Using for loop : {strholder}") # Using for loop : cba  
'''
Using Loop Concatenation (Not Efficient)
rev = ""
for ch in text:
    rev = ch + rev

---> ⏱ Time Complexity: O(n²) ❌

Each concatenation creates a new string.

Copying happens again and again.

---> 💾 Space Complexity: O(n)

👉 Not recommended for large strings.

'''

# Convert to List + Reverse In-Place

charListOfChar = list(myStr) # ['a', 'b', 'c']
charListOfChar.reverse() # ['c', 'b', 'a']
revStr3 = "".join(charListOfChar) # "cba"
print(f"Using list + reverse() : {revStr3}") # Using list + reverse
