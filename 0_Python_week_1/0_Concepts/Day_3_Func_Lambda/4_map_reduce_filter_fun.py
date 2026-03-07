


# map(fun, it) 
# reduce
# filter()


# 1️⃣  map(fun, it) :
print("\n\n ---> 1 - map(fun, it) <------- \n")

'''
In Python, map() is a built-in function that applies a function to every item in an iterable (like a list, tuple, etc.) and returns a map object (iterator).
'''
# map(function, iterable)
'''
function → The function to apply to each element
iterable → The collection (list, tuple, etc.)
'''
# 1️⃣ Basic Example
def double_element(num): 
    return num**2


nums = [1, 2, 3, 4, 5]
print(f"Original list : {nums}")
result = map(double_element, nums) # ✔ map() applies double_element() to each element in nums.
print(f"Ex:1 ==> after doubling the list : {list(result)}") # casting to iterable is must to work with data


# 2️⃣ Using map() with lambda
numbers = [4,5,6,10,11]
print(f"Original List : {numbers}")
result = map(lambda x: x*2, numbers)
print(f"Ex:2 ==> List after doubling each element through Lambda function: {list(result)}  ")


# 3️⃣ Example with Multiple Lists
l1 = [1,3,5,6,7]
l2 = [11, 5, 10,4, 10] # if we have any extra element in any of the list then that lambda operation will be skipped.
print(f"LIST1 : {l1} and \nLIST2 : {l2}")
# multiply corresponding elements of the lists
result = map(lambda x, y : x*y , l1, l2 )
print(f"Ex:3 ==> after multiplying corresponding element of above list : {list(result)}")



# 2️⃣ filter(function, iterable) : 

'''
filter() filters elements based on a condition. Or
Select elements based on condition.
Selects elements that match a condition.
Returns only items where the function is True.
It returns only elements where the function returns True.

filter(function, iterable)

'''
print("\n\n ---> 2 - filter(fun, it) <------- \n")

# example - ✔ Keeps only odd numbers.
print(" from a give list print only odd numbers : ")
nums = [1,4,6,8,3,9,7,2]
print(f"Original List : {nums}")
# filter only the odd numbers from the give list :
result = filter(lambda x : x%2 != 0, nums)
print(f"Ex-1 ==> Only odd number filtered from the above list : {list(result)}")

# 3️⃣ reduce(function, iterable):
'''
reduce() reduces the iterable into a single value by repeatedly applying the function.
⚠️ It is in the functools module, so you must import it.

Optonal -> If 'initial' is present, it is placed before the items of the iterable in the calculation, and serves as
            a default when the iterable is empty.

        ->    reduce(function, iterable, initial)
             function → operation to apply
             iterable → list/tuple etc.
             initial → starting value (optional)

        ->  In reduce(), the initial value is an optional starting value that is used before the elements of the iterable during the calculation.
        -> It is equivalent to adding the initial value at the beginning of the list.


--> Combines all elements into 'one single value'.
--> Performs cumulative operations.
--> perform from left to right to reduce it to the single value.


Syntax:

    from functools import reduce
    reduce(function, iterable)

'''

print("\n\n ---> 3 - reduce(function, iterable) <------- \n")

from functools import reduce
# example - ✔ Adds all numbers together.
nums = [1, 2, 3, 4, 5]

def sum_all(a, b): # for summing or adding we obvously need two params . That's why in reduce we use Cumulative word.
    return a+b


result = reduce( sum_all, nums) # we dont pass params while calling the funcitons. if we are kinf of lambda we defining 
print(f"Ex:-1 ==>  sum all number of above 'list - {nums} ' by reduce with normal function calling in reduce() : {result}")

result_reduce = reduce(lambda x,y: x+y, nums)
print(f"Ex:-1 ==>  sum all number of above 'list - {nums} ' by Lambda function in reduce() : {result_reduce}")
'''
Step process:

1+2 = 3
3+3 = 6
6+4 = 10
10+5 = 15
'''

# Example - 2 : Multiply all numbers
nums = [1, 2, 3, 4]
result_multiply_all = reduce(lambda x,y:x*y, nums)
print(f"Ex:-2 ==>  Multiply all numbers of above 'list - {nums} ' by Lambda function in reduce() : {result_multiply_all}")
# 24
'''
1 * 2 = 2
2 * 3 = 6
6 * 4 = 24
'''

# Example-3 : Find the largest number
nums = [10, 25, 7, 40, 15]
result_get_largest = reduce( lambda x, y : x if x>y else y  , nums)
print(f"Ex:-3 ==>  Find largest element from the above 'list - {nums} ' by Lambda function in reduce() : {result_get_largest}")
# 40
# NOTE : ✔ reduce() compares numbers and keeps the largest value.
'''
Steps :

Step 1:
x = 10, y = 25
10 > 25 → False
Result → 25

Step 2:
x = 25, y = 7
25 > 7 → True
Result → 25

Step 3:
x = 25, y = 40
25 > 40 → False
Result → 40

Step 4:
x = 40, y = 15
40 > 15 → True
Result → 40

'''

# Example with initial value
from functools import reduce

nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, nums, 10)
print(result)
'''
10 + 1 = 11  # ✔ The initial value (10) starts the calculation. otherwise it will be like this - 1 +2 = 3
11 + 2 = 13
13 + 3 = 16
16 + 4 = 20

'''
# Why is initial value useful?
'''
1️⃣ Sets a starting value

2️⃣ Prevents errors when iterable is empty

reduce(lambda x, y: x + y, [], 0)
result = 0

Without initial value → Error

'''

# Is initial present in map() and filter()???????????????  ❌ No 
'''
| Function   | Has Initial Value? | Reason                          |
| ---------- | ------------------ | ------------------------------- |
| `map()`    | ❌ No               | It only transforms each element |
| `filter()` | ❌ No               | It only selects elements        |
| `reduce()` | ✅ Yes              | It accumulates into one value   |


'''




