# PYTHON FUNCTIONS & LAMBDA – DAY 3 (README)

Functions are reusable blocks of code that perform a specific task.  
Lambda functions are anonymous, single-line functions for quick operations.

---

## ✅ Objectives

By the end of this day, you should be able to:  
- Write modular, reusable functions  
- Use `*args` and `**kwargs` for variable inputs  
- Implement lambda functions for concise operations  
- Apply `map()` and `filter()` for data transformations  
- Build small practical data cleaning and transformation scripts  

---

## 📌 Revision Checklist

1. **Function Basics**  
   - `def` keyword  
   - Parameters & return values  

2. **`*args` and `**kwargs`**  
   - Variable positional arguments  
   - Variable keyword arguments  

3. **Lambda Functions**  
   - Single-line anonymous functions  
   - Often used with `map()`, `filter()`, and `sorted()`  

4. **`map()`, `filter()`, `reduce()`**  
   - `map()`: Apply function to each element  
   - `filter()`: Select elements based on condition  
   - `reduce()`: Cumulative computation (from `functools`)  

5. **Practical Examples**  
   - Reusable data cleaning function  
   - Validate email format  
   - Transform list of dictionaries  

---

## 1️⃣ Function Basics

**Example: Simple function**

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

```
# Python Functions, *args, **kwargs, and Lambda Functions

## Key Ideas
- Functions avoid code repetition
- Return values allow reusable output
- Improve readability and maintainability

## 2️⃣ *args and **kwargs

### Variable Positional Arguments (*args)
```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))  # Output: 6
```

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)

```

## Notes / Interview Tips

- `*args` → tuple of positional arguments
- `**kwargs` → dictionary of keyword arguments
- Useful when the number of inputs is not fixed



## 3️⃣ Lambda Functions

### Single-line Anonymous Functions
```python
square = lambda x: x**2
print(square(5))  # Output: 25
```

### Using Lambda with `map()`
```python
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16, 25]
```

### Using Lambda with filter():
```python
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # [2, 4]

```

### Example: Find the Largest Number using `reduce()`
`NOTE:` ✔ reduce() compares numbers and keeps the largest value.
```python
from functools import reduce

nums = [10, 25, 7, 40, 15]

largest = reduce(lambda x, y: x if x > y else y, nums)
print(largest)
# output - 24
```

## Notes / Interview Tips
- Lambdas are for short, throwaway functions
- `map()` & `filter()` → concise alternatives to for-loops
- `map()` → apply transformation to all items
- `filter()` → select items based on condition
- Lambdas + `map`/`filter` are frequently used in data pipelines

## 4️⃣ Practical Examples

### A. Reusable Data Cleaning Function
```python
def clean_data(data_list):
    return [item.strip().lower() for item in data_list]

raw_data = [" Alice ", "BoB ", " CHARLIE"]
print(clean_data(raw_data))  # ['alice', 'bob', 'charlie']
```

### B. Validate Email Format
```python
def is_valid_email(email):
    return "@" in email and "." in email

emails = ["test@example.com", "invalidemail.com"]
valid_emails = list(filter(is_valid_email, emails))
print(valid_emails)  # ['test@example.com']
```

### C. Transform List of Dictionaries
```python
users = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
transformed_users = list(map(lambda x: {"name": x["name"].upper()}, users))
print(transformed_users)
# [{'name': 'ALICE'}, {'name': 'BOB'}, {'name': 'CHARLIE'}]
```


## 🧠 Easy Way to Remember

| Function | Keyword  | Meaning |
|---------|----------|--------|
| **map()** | Modify  | Change every element |
| **filter()** | Select | Keep elements that match a condition |
| **reduce()** | Combine | Merge all elements into one value |

### Quick Memory Trick

map → **modify data**  
filter → **select data**  
reduce → **combine data**

### Note - 🔹 Bonus trick (very Pythonic)

Instead of map, many Python developers prefer list comprehension:

```python
nums = [1,2,3]
result = [x*x for x in nums]
# OUTPUT-  [1,4,9]

```