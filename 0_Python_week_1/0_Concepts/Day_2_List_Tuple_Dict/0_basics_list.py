'''
--> What is a List?

* A list is a data structure that:
* Stores multiple values
* Is ordered
* Is mutable (can be changed)
* Allows duplicate values
* Think of it like a container: You can put different items in it, and you can change what's inside.

## Python lists are very flexible:

* Can contain duplicate items
* Mutable: items can be modified, replaced, or removed
* Ordered: maintains the order in which items are added
* Index-based: items are accessed using their position (starting from 0)
* Can store mixed data types (integers, strings, booleans, even other lists)
'''


print("-----> Creating Lists <-----")

# create empty list in python :
emptyList = []
print("Empty List : " , emptyList) # Empty List :  []

# List of integers:
intList = [1,3,4,6,7]
print(f"Print Direct List : {intList}") # Print Direct List : [1, 3, 4, 6, 7]

# List of Mixed data types:
mixedDataList = [1 ,3, True, 5.6 ,6.666, "Hello" , "CCC"]
print(f"Lis of mixed  dataType values : {mixedDataList}") # Lis of mixed  dataType values : [1, 3, True, 5.6, 6.666, 'Hello', 'CCC']


print("----->  Accessing List Elements <-----") # Accessing List Elements
print(f"Accessing 1st element from asc order index of List- {intList} ====>  {intList[0]}") # Accessing 1st element from asc order index : 1
print(f"Accessing 1st element from desc order index of List or through Negivative Index- {intList} ====>  {intList[-1]}") # Accessing 1st element from desc order index : 7


print(f" 2nd Element of above list - intList[1] : {intList[1]}")

print("---> Accessing List Elements using Slicing <---")
print(f"List - {intList} : Slicing from 2 to 4th elements [a:b:step] == [startIndx:endIndx:Step], b index is excluded: {intList[1:4]}")

print("----->  Accessing List Elements using Loop <-----")

print("###  Using normal for loop to access list elements ###")
print(f"List - {intList} : Accessing elements using normal for loop : ")
for i in range(len(intList)):
    print(f"{i}th elemnt for List is : {intList[i]}")
    

print("###  Using for-each loop to access list elements ###")
print(f"List - {intList} : Accessing elements using for-each loop : ")
ind  = 0
elePos = ind+1
for ele in intList:
    print(f"{elePos}th element of list is : {ele}")
    elePos +=1

'''
-----> Creating Lists <-----
Empty List :  []
Print Direct List : [1, 3, 4, 6, 7]
Lis of mixed  dataType values : [1, 3, True, 5.6, 6.666, 'Hello', 'CCC']
----->  Accessing List Elements <-----
Accessing 1st element from asc order index of List- [1, 3, 4, 6, 7] ====>  1
Accessing 1st element from desc order index of List or through Negivative Index- [1, 3, 4, 6, 7] ====>  7
 2nd Element of above list - intList[1] : 3
---> Accessing List Elements using Slicing <---
List - [1, 3, 4, 6, 7] : Slicing from 2 to 4th elements [a:b:step] == [startIndx:endIndx:Step], b index is excluded: [3, 4, 6]
----->  Accessing List Elements using Loop <-----
###  Using normal for loop to access list elements ###
List - [1, 3, 4, 6, 7] : Accessing elements using normal for loop : 
0th elemnt for List is : 1
1th elemnt for List is : 3
2th elemnt for List is : 4
3th elemnt for List is : 6
4th elemnt for List is : 7
###  Using for-each loop to access list elements ###
List - [1, 3, 4, 6, 7] : Accessing elements using for-each loop : 
1th element of list is : 1
2th element of list is : 3
3th element of list is : 4
4th element of list is : 6
5th element of list is : 7

'''