d = {'a': 1, 'b': 2, 'c': 3}
unp = {**d, 'f' : 55}
print(unp)

scores = {"Alice": 90, "Bob": 80, "Charlie": 85}
items_list = list(scores.items())
print(items_list)

for i in range(len(items_list)):
    print(f"2nd element of tuple at index {i} is {items_list[i][1]}")


# count charcter in string :
s = "abcccdddnnnvv"
target_char1 = 'n'
target_char2 = 'c'
target_char3 = 'p'
print(f"count '{target_char1}' in string '{s}' is : {s.count(target_char1)}")
print(f"count '{target_char2}' in string '{s}' is : {s.count(target_char2)}")
print(f"count '{target_char3}' in string '{s}' is : {s.count(target_char3)}")
