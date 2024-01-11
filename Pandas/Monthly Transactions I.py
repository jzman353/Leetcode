"""
1193. Monthly Transactions I
Solved
Medium
Topics
Companies
SQL Schema
Pandas Schema
Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order.

The query result format is in the following example.

Example 1:

Input:
Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
Output:
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+
"""

import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    df_all = transactions.groupby(dropna=False, by=[pd.Grouper(key='trans_date', freq='M'), transactions.country]).agg(trans_total_amount=('amount', 'sum'), trans_count=('id', 'count')).reset_index()
    df_all['trans_date'] = df_all['trans_date'].dt.strftime('%Y-%m')
    df_approved = transactions[transactions['state'] == 'approved']
    df_approved = df_approved.groupby(dropna=False, by=[pd.Grouper(key='trans_date', freq='M'), df_approved.country]).agg(approved_total_amount=('amount', 'sum'), approved_count=('id', 'count')).reset_index()
    df_approved['trans_date'] = df_approved['trans_date'].dt.strftime('%Y-%m')
    df = pd.merge(df_all, df_approved, how='outer', on=['trans_date', 'country'])
    df.rename(columns={"trans_date":"month"}, inplace=True)
    df[['trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount']] = df[['trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount']].fillna(0)
    return df[['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount']]

"""
import pandas as pd

def monthly_transactions(df: pd.DataFrame) -> pd.DataFrame:
    df['month']=df['trans_date'].dt.strftime('%Y-%m')
    df['approved_count']=df['state'].map(lambda x : 1 if x=='approved' else 0)
    df['approved_total_amount']=df['amount']*df['approved_count']
    df=df.groupby(['month','country'],as_index=False).agg(trans_count=('state','count'),approved_count=('approved_count','sum'),trans_total_amount=('amount','sum'),approved_total_amount=('approved_total_amount','sum'))
    return df
"""