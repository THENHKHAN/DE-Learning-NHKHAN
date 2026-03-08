
import json

json_location = '0_Python_week_1/data/schemas.json'
file_pointer = open(json_location, 'r')
schemas = json.load(file_pointer) # json.load(): Reads JSON from a file Converts it to Python objects
print(" Schemas data from json file and loaded : ", schemas) 
print("Type of schema after load :  ", type(schemas))  # Type of schema after load :   <class 'dict'>
# This is a Python dictionary.

# load() → file
# loads() → string
'''
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)
'''

# find departments info  values :
departs = schemas['departments']
print(departs) # [{'column_name': 'department_id', 'data_type': 'integer', 'column_position': 1}, {'column_name': 'department_name', 'data_type': 'string', 'column_position': 2}]

print("\n------- Departs data --------\n")
for info in departs:
    # print(f"info type : {type(info)}") # info type : <class 'dict'>
    for k , v in info.items():
        print(f"{k}-> {v} \n ")


# find all the keys or column of schema :

keys_schema = schemas.keys()
print(f"keys of schemas : {list(keys_schema)}") # ['departments', 'categories', 'orders', 'products', 'customers', 'order_items']


# sort the schema orders by  column_position - In DESC
column_details = schemas.get('orders') # [{'column_name': 'order_id', 'data_type': 'integer', 'column_position': 1}, {'column_name': 'order_date', 'data_type': 'string', 'column_position': 2}, {'column_name': 'order_customer_id', 'data_type': 'timestamp', 'column_position': 3}, {'column_name': 'order_status', 'data_type': 'string', 'column_position': 4}]
print("order columns details : " , column_details)

sorted_orders_by_column_position = sorted (column_details, key=lambda x: x['column_position'] , reverse=True)
print(f"Sorted orders by column_position : {sorted_orders_by_column_position}")
# [{'column_name': 'order_status', 'data_type': 'string', 'column_position': 4}, {'column_name': 'order_customer_id', 'data_type': 'timestamp', 'column_position': 3}, {'column_name': 'order_date', 'data_type': 'string', 'column_position': 2}, {'column_name': 'order_id', 'data_type': 'integer', 'column_position': 1}]

# find the columns from the sorted_orders_by_column_position?? so we can see sorted coloumn
columns = [col['column_name'] for col in sorted_orders_by_column_position]
print("sorted cols: " , columns)
# sorted cols:  ['order_status', 'order_customer_id', 'order_date', 'order_id']