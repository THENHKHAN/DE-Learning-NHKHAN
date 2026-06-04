
import pandas as pd

csv_path = '0_Python_week_1/data/orders/part-00000.csv'
df_temp = pd.read_csv(csv_path, header=None) # headers = None means pandas automatically defined columns name as 0 ,1,2 ...
print( "Csv without header : \n\n " , df_temp) # but if we skip then it will automatically assume the 1st row of dataframe as header.

# Here in this csv we dont have headers/ columns so lets create and add while reading.

orders_column = [
    'order_id' , 'order_date' , 'order_customer_id', 'order_status'
]
# csv we header defined manually :

orders_df = pd.read_csv(csv_path, names=orders_column) # once we defined names then we dont need to define the header since it will automatically infer.
print(f"\n\n CSV with manual Header defined :  \n\n {orders_df}")

print(f"Cols name : {list(orders_df.columns)}") # ['order_id', 'order_date', 'order_customer_id', 'order_status']