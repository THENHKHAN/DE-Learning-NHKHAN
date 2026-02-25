# 📘 Python List Slicing — Clear Reference Guide


lst = [0, 1, 2, 3, 4, 5]

# 1️⃣ Basic Slice Syntax
'''
list[start : stop : step]

start → index to begin from (included)

stop → index to stop at (NOT included)

step → how many positions to move each time

    Default = 1
'''

2️⃣ Default Step (Forward Slicing)

'''
lst[1:4]
lst[1:4:1]
✅ Both give: [1, 2, 3]

✔ Why?

    Start at index 1
    Stop before index 4
    Move forward by 1 (default step)


So:
Index:  0  1  2  3  4  5
Value: [0, 1, 2, 3, 4, 5]
           ↑  ↑  ↑
'''

3️⃣ Negative Step (Backward Slicing)

'''
When step is negative, Python moves right → left.

    ❌ Example That Returns Empty

lst[1:4:-1]
Result: : []

❗ Why?

Start at index 1
Step = -1 → move backward
Stop at index 4
But index 4 is to the right of 1.
You cannot go backward from 1 and reach 4.

So Python returns an empty list.
'''

4️⃣ Correct Backward Example

'''
lst[4:1:-1]
Result:: [4, 3, 2]

✔ Why?

Start at index 4
Move backward
Stop before index 1

Index:  0  1  2  3  4  5
Value: [0, 1, 2, 3, 4, 5]
                 ↑  ↑  ↑
                 
'''
5️⃣ Reverse Entire List

'''
lst[::-1]
Result: [5, 4, 3, 2, 1, 0]

✔ Why?

No start → begin at end -- WHY not START - SINCE we have -1 as step, it starts from the end of the list.

No stop → go to beginning

Step = -1 → move backward


'''

🔑 Golden Rule to Remember

'''
🔑 Golden Rule to Remember
✅ If step is pppppppppppositive:

start must be less than stop

✅ If step is nnnnnnnnnnnegative:

start must be greater than stop

Otherwise → result is []
'''
