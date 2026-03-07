

'''
3️⃣ Lambda Functions (Anonymous Functions)

Lambda functions are small, single-line anonymous functions.
They are commonly used for short operations where defining a full function is unnecessary.
'''

print("\n\n ---> 1 - Basic Lambda Function <------- \n")


def square_num(num) :
    return num**2

n = 20
print(f"Normal function square({n}) wihtout lambda : {square_num(n)}")

# same one single operation can be eaisly done by lambda

# Lambda equivalent

square_lambda = lambda x: x**2
p = 10
print(f"lambda square({p}) : {square_lambda(p)}") 

print("\n\n ---> 2 - Lambda with map() <------- \n")

# map() applies a function to every element in an iterable
nums = [1, 2, 3, 4, 5]
print(f"Original list : {nums}")
# map(): 
'''
In Python, map() is a built-in function that applies a function to every item in an iterable (like a list, tuple, etc.) 
and returns a map object (iterator). And then we can  cast to any iterable like list.
'''

# map(function, iterable) - function could be lambda funcitons as well.
'''
function → The function to apply to each element
iterable → The collection (list, tuple, etc.)
'''

square_of_each = map(square_num, nums)
print(f"square all element of ' list- {nums}' square without lambda but similar to lamda : {list(square_of_each)}") 
result = map(lambda x: x**2 , nums)
print(f"square all element of ' list- {nums}' square WiTH lambda : {list(result)}") 


print("\n\n ---> 3 - Lambda with filter() <------- \n")
# filter() selects elements based on a condition

num = [3, 5, 10, 22, 4 ,6]
print(f"Original list : {nums}")

result = filter(lambda x: x%2 != 0 , num)
print(f"Even numbers using lambda + filter : {list(result)}")


print("\n\n ---> 4 - Lambda with sorted() <------- \n")
# Lambda is often used as a key function
students = [
    {"name" : "Noorul" , "age" : 38 },
    {"name" : "Huda" , "age" : 50 },
    {"name" : "Khan" , "age" : 25 }
]
# sort the students by their age ??

# we can  use normal looking - by converting to list of tuples etc  but for now lets use sorted and lambda 
sorted_students  = sorted(students, key=lambda x : x ['age'] )  #  x will be whole dictionary like - {"name" : "Noorul" , "age" : 38 }, so form there we are acceesing age. it will sort in asc but if we revers = True then it will sort in Desc order.
'''
sorted() does NOT modify the original list.
It returns a new sorted list.
'''
print("Students sorted by age:\n")
for stud in sorted_students:
    print(stud)

'''
{'name': 'Khan', 'age': 25}
{'name': 'Noorul', 'age': 38}
{'name': 'Huda', 'age': 50}

'''

'''
| Function      | Modifies Original | Returns New List |
| ------------- | ----------------- | ---------------- |
| `sorted()`    | ❌ No              | ✅ Yes            |
| `list.sort()` | ✅ Yes             | ❌ None           |


students.sort(key=lambda x: x['age'])

sorted(list) → returns new list
list.sort()  → modifies existing list
'''


'''
Interview Tips:

    Lambda functions are anonymous (no function name).
    They must be single expressions (no statements).
    Commonly used with:
        map() → transform elements
        filter() → select elements
        sorted() → custom sorting key
    Best used for small, throwaway functions.

    Syntax:
        lambda arguments : expression

Example:
    lambda x: x * 2
'''
