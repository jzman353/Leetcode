"""
1251. Average Selling Price
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Prices

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the price of the product_id in the period from start_date to end_date.
For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.


Table: UnitsSold

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the date, units, and product_id of each product sold.

Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input:
Prices table:
+------------+------------+------------+--------+
| product_id | start_date | end_date   | price  |
+------------+------------+------------+--------+
| 1          | 2019-02-17 | 2019-02-28 | 5      |
| 1          | 2019-03-01 | 2019-03-22 | 20     |
| 2          | 2019-02-01 | 2019-02-20 | 15     |
| 2          | 2019-02-21 | 2019-03-31 | 30     |
+------------+------------+------------+--------+
UnitsSold table:
+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |
+------------+---------------+-------+
Output:
+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1          | 6.96          |
| 2          | 16.96         |
+------------+---------------+
Explanation:
Average selling price = Total Price of Product / Number of products sold.
Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96
"""

import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(prices, units_sold, how='left')
    df = df[(df['purchase_date'] <= df['end_date']) & (df['purchase_date'] >= df['start_date'])]
    df['total_price'] = df['units'] * df['price']
    df_sum = df.groupby('product_id')[['total_price', 'units']].sum().reset_index('product_id')
    df_sum['average_price'] = (df_sum['total_price'] / df_sum['units']).round(2)
    df_all_prod_ids = prices.groupby('product_id')['price'].count()
    final = pd.merge(df_sum, df_all_prod_ids, how="outer", on="product_id").fillna(0)
    return final[['product_id', 'average_price']]

"""
def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(prices,units_sold, how='left',on='product_id')
    df = df[(df['purchase_date']>=df['start_date']) & (df['purchase_date']<=df['end_date'])]
    df['Total_price']=(df['price']*df['units'])
    df = df.groupby('product_id')[['Total_price','units']].sum().reset_index()
    df['average_price']= round(df['Total_price']/df['units'],2)
    df=df[['product_id','average_price']]
    return pd.merge(df[['product_id','average_price']],prices[['product_id']].drop_duplicates(),how='right',on='product_id').fillna(0)
"""