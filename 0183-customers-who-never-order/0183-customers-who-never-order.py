import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cust = customers
    ord = orders
    df = cust[~cust['id'].isin(ord['customerId'])][['name']]
    return df[['name']].rename(columns={'name':'Customers'})