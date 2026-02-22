# 🚀 Week 1 – Python Strengthening (Detailed Plan)

Since you already know basic Python, this week focuses on:

- Writing clean production-level code
- Thinking like a data engineer
- Handling files, errors, and logs
- Preparing for PySpark logic

---

## 🎯 WEEK 1 GOAL

By the end of Week 1, you should be able to:

- ✅ Write Python without hesitation  
- ✅ Handle CSV / JSON files  
- ✅ Use functions & classes properly  
- ✅ Handle exceptions cleanly  
- ✅ Write modular, production-style code  

---

# 📅 DAILY PLAN – WEEK 1

## 🟢 DAY 1 – Core Python Refresher

### Study:
- Variables
- Data types
- Strings
- Input / Output
- Type conversion

### Practice:
- Reverse a string
- Check palindrome
- Count vowels in a string

Night:
- Solve 5 beginner problems on HackerRank

---

## 🟢 DAY 2 – Lists & Dictionaries

### Study:
- List operations
- List comprehension
- Dictionary usage
- Nested dictionaries

### Practice:
- Remove duplicates from list
- Count word frequency
- Sort dictionary by values

---

## 🟢 DAY 3 – Functions & Lambda

### Study:
- Functions
- *args, **kwargs
- Lambda functions
- map(), filter()

### Practice:
- Write reusable data cleaning function
- Validate email format
- Transform list of dictionaries

---

## 🟢 DAY 4 – OOP Basics

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount

    def display_info(self):
        return f"{self.name} earns {self.salary}"

```
---

## 🟢 DAY 5 – File Handling (VERY IMPORTANT)

### Study:
- Reading CSV files using `csv` module
- Writing CSV files
- Reading JSON files
- Writing JSON files
- Using `with open()` properly
- Understanding file modes (`r`, `w`, `a`)

### Practice:
- Read a sales CSV file
- Filter rows based on condition (e.g., amount > 1000)
- Handle missing/null values
- Write cleaned data to a new CSV file
- Convert cleaned data to JSON format

This simulates real-world ETL logic.

---

## 🟢 DAY 6 – Mini Project (3–5 Hours)

### 📌 Project: Basic ETL Script

Build a small end-to-end ETL pipeline.

### Steps:
1. Read a CSV file
2. Clean null or invalid values
3. Convert date column to proper format
4. Aggregate totals (e.g., total sales per product)
5. Write output to JSON file
6. Add proper `try/except` blocks
7. Add logging using `logging` module

### Learn:
- Basic logging setup
- Logging levels (`INFO`, `WARNING`, `ERROR`)
- Writing logs to a file (`logs.txt`)

---

## 🟢 DAY 7 – Advanced Python Concepts

### Study:
- List vs Generator (memory difference)
- Basic idea of decorators
- Virtual environments (`venv`)
- `requirements.txt` usage

### Practice:
- Create a virtual environment
- Activate it
- Install `pandas`
- Perform a small data transformation using pandas
- Generate a `requirements.txt` file
+
---

# ⏳ Total Time Commitment

- Weekdays: ~10–12 hours  
- Weekend: ~8–10 hours  
- Total: ~20 hours solid Python practice
