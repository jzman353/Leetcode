"""
1070. Product Sales Analysis III
Medium
Topics
Companies
SQL Schema
Pandas Schema
Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.

Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.


Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

Return the resulting table in any order.

The result format is in the following example.

Example 1:

Input:
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
Output:
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+
"""


import pandas as pd

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199

"""
#TLE
def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby('product_id')['year'].min().reset_index()

    df1 = pd.DataFrame()
    for index, row in df.iterrows():
        df2 = sales[(sales['year']==row['year']) & (sales['product_id']==row['product_id'])]
        df1 = pd.concat([df1,df2]).drop_duplicates().reset_index(drop=True)

    df1.rename(columns={"year": "first_year"}, inplace=True)
    df1.drop(columns=['sale_id'], inplace=True)

    return df1
"""
#100%
def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    sales.drop(columns=['sale_id'], inplace=True)
    df = sales[sales['year'] == sales.groupby('product_id')['year'].transform('min')]
    df.rename(columns={"year": "first_year"}, inplace=True)

    return df

sales = pd.read_csv('Product Sale Analysis III Input1.csv')
l = list(sales.columns)
for i in range(len(l)):
    l[i] = l[i].strip()
sales.columns = l
print(sales_analysis(sales, pd.DataFrame({"test":[1]})))

