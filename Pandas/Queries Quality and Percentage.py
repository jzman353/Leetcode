"""
1211. Queries Quality and Percentage
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Queries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The position column has a value from 1 to 500.
The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.

We define query quality as:

The average of the ratio between query rating and its position.

We also define poor query percentage as:

The percentage of all queries with rating less than 3.

Write a solution to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input:
Queries table:
+------------+-------------------+----------+--------+
| query_name | result            | position | rating |
+------------+-------------------+----------+--------+
| Dog        | Golden Retriever  | 1        | 5      |
| Dog        | German Shepherd   | 2        | 5      |
| Dog        | Mule              | 200      | 1      |
| Cat        | Shirazi           | 5        | 2      |
| Cat        | Siamese           | 3        | 3      |
| Cat        | Sphynx            | 7        | 4      |
+------------+-------------------+----------+--------+
Output:
+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog        | 2.50    | 33.33                 |
| Cat        | 0.66    | 33.33                 |
+------------+---------+-----------------------+
Explanation:
Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33

https://stackoverflow.com/questions/45223778/is-bankers-rounding-really-more-numerically-stable

#6%
"""

import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['percentage']=1e-10+queries['rating']/queries['position']
    queries.drop(columns=['result', 'position'], inplace=True)
    quality = queries.groupby(['query_name']).mean()['percentage'].round(2).reset_index(name='quality')
    poor_query_percentage = ((100*queries[queries["rating"] < 3].groupby(['query_name']).count()['rating'])/(queries.groupby(['query_name']).count())['rating']).round(2).reset_index(name='poor_query_percentage')
    new = pd.merge(quality, poor_query_percentage, how='left')
    new = new.fillna(0)
    return new

"""
def queries_stats(df: pd.DataFrame) -> pd.DataFrame:
    df = df.assign(quality = df.rating / df.position + 1e-10, poor_query_percentage = (df.rating < 3).astype(int)*100)
    return df.groupby("query_name", as_index = False)[["quality","poor_query_percentage"]].mean().round(2)


For anyone else learning, these two are the same:

    return df.groupby("query_name", as_index = False)[["quality","poor_query_percentage"]].mean().round(2)
    return df.groupby("query_name", as_index =  True)[["quality","poor_query_percentage"]].mean().round(2).reset_index()
The first one is not the default, as_index=False keeps the groupby column as a column. Then you can compute means and round and whatever.

The second one is the default, as_index=True makes the groupby column the row index of the resulting dataframe. So the .mean() result is a DataFrame with query_name as the row index. Then reset_index() converts the query_name index back into a column, prepends it to the existing columns, and sets the new index to be row numbers 0, 1, .., N-1.
"""
