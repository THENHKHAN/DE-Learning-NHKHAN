
# Create a dictionary of squares for numbers 1 to 5
squares = {}
for x in range(1,6):
    squares[x] = x**2 
print("Dictionary of squares from 1 to 5 : " , squares)

# with dictionary comprehension
squares_comp = {key:key*key for key in range(1,6)}
print("Dictionary of squares from 1 to 5 using comprehension : " , squares_comp)

# Q - find generate only even squares from 1 to 8 using dictionary comprehension
lst = [1,2,3,4,5,6,7,8]
even_numbers_squares = {num:num**2 for num in lst if num % 2 == 0 }
print("Even numbers squares from 1 to 8 using comprehension : " , even_numbers_squares)

'''
Notes / Interview Tips

    --> Dictionary comprehension is very fast and concise
    --> Often asked in interviews: “Create a dictionary from a list with a condition”
    --> You can combine with nested loops for more advanced problems


'''