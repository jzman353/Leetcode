"""
1164. Product Price at a Given Date
Solved
Medium
Topics
Companies
SQL Schema
Pandas Schema
Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.


Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
Output:
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
"""
#64%
import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    s = set(products['product_id'])
    products = products[products['change_date'] <= '2019-08-16']
    products = products.sort_values(by=['change_date'])
    df = products.groupby('product_id')['new_price'].last().reset_index()
    df.rename(columns={"new_price": "price"}, inplace=True)
    l = set(df['product_id'])
    for i in s:
        if i not in l:
            df = pd.concat([df,pd.DataFrame({"product_id":[i], "price":[10]})])
    return df


"""
def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    temp_df = products[products['change_date']<='2019-08-16'].sort_values(by='change_date', ascending=False)
    temp_df = temp_df.groupby('product_id')['new_price'].first().to_frame()
    res_df = pd.Series(products.product_id.unique()).to_frame('product_id').merge(temp_df, how='left', on='product_id').fillna(10)
    res_df.columns = ['product_id', 'price']
    return res_df
"""