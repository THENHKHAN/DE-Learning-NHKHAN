
# Check if a string is a palindrome or not?

# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
# examples : aba , nitin, madam. NOT - abc , hello





my_str1 = "Noorul"
my_str2 = "nitin"
reversed_str1 = my_str1[::-1]
reversed_str2 = my_str2[::-1]
print(f"Is {my_str1} a plaindrome? by  slciing operator --> {my_str1 == reversed_str1}")
print(f"Is {my_str2} a plaindrome? by  slciing operator --> {my_str2 == reversed_str2}")


'''

4. Time & Space Complexity

Your two-pointer approach:
    Time Complexity: O(n)
    Space Complexity: O(n) (because of the cleaned string)

    NOTE - we can also check without creating a new string by using two pointers to skip spaces and compare characters directly, which would reduce space complexity to O(1).
'''
def is_palindrome(s):
    s = s.replace(" " , "").lower() # remove spaces and convert to lowercase

    # edge case : empty string and single character string are palindromes
    if len(s) <=1 :
        return True

    l = 0
    r = len(s) -1 

    while l<r :
        if (s[l] != s[r]) :
            return False
        l +=1
        r -=1
    return True

# shorter
def is_palindrome_short(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

my_str3 = "huda"
print("\n\n-----> Using for loop to reverse the string DSA Type <-----\n")
print(f"Is {my_str3} a plaindrome? by  for loop --> {is_palindrome(my_str3)}")
print(f"Is {my_str2} a plaindrome? by  for loop --> {is_palindrome(my_str2)}")
print(f"Is {my_str1} a plaindrome? by  for loop --> {is_palindrome(my_str1)}")