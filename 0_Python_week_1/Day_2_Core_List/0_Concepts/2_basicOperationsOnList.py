

a = [1, 2, 3, 4, 5] # List of integers
print(f"Original List: {a}")
# 1- Adding Elements into List by append(element) method : Adds an element at the end of the list.
a.append(100) # Adds 100 at the end of the list
print(f"After appending 100 usig append method: {a}")

# 2-  Inserting an element at a specific index insert(index, element) : Adds an element at a specific position.
a.insert(3, 300) # Inserts 300 at index 3
print(f"Aftr inserting 300 at index 3 using insert method: {a} ")


# 3- extend() : Adds all elements of an iterable (like another list) to the end of the list. 
                # Adds multiple elements to the end of the list.

str2 = [11, 33, 55, 77, 99]
print(f"Original List: {a}")
a.extend(str2) # Extends list a by adding elements of str2
print(f"After extending list After extend ([11, 33, 55, 77, 99])  a with str2 using extend() method: {a}")

#  Clear() : Removes all elements from the list, leaving it empty.
print(f"Original List: {a}")
a.clear() # Clears all elements from the list a
print(f"After clearing the list a using clear() method: {a}")

print("###################    Updating Elements into List   ###############################")

str1 = [22, 44, 55, 77, 99]
print(f"Original List: {str1}")
# 1- Updating an element at a specific index : You can update an element by assigning a new value to a specific index.
str1[2] = 6666
print(f"After updating element at index 2 to 6666: {str1}")


print("###################    Deleting Elements from List Or Removing Elements from List  ###############################")
# Removes the first occurrence of an element.
a = [1, 2, 3, 4, 5] # List of integers
print(f"Original List: {a}")
# 1- Removing an element by value remove(element) : Removes the first occurrence of a specified value from the list.
a.remove(4) # Removes the first occurrence of 4 from the list
print(f"After removing 4 using remove() method: {a}")

# if element is not found in the list, it raises a ValueError.
# a.remove(10) # This will raise ValueError because 10 is not in the

print("")