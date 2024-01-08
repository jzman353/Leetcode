'''
610. Triangle Judgement
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Triangle

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.


Report for every three line segments whether they can form a triangle.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output:
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+

15%
'''

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    #https://www.wikihow.com/Determine-if-Three-Side-Lengths-Are-a-Triangle
    def label_triangle_possibility(row):
        if (row['x']+row['y']>row['z']) & (row['x']+row['z']>row['y']) & (row['z']+row['y']>row['x']):
            return 'Yes'
        else:
            return 'No'
    triangle['triangle'] = triangle.apply(label_triangle_possibility, axis=1)
    return triangle

"""
import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    output=[]
    for index, row in triangle.iterrows():
        x, y, z = abs(row['x']), abs(row['y']), abs(row['z'])
        if x+y>z and x+z>y and y+z>x:
            output.append('Yes')
        else:
            output.append('No')

    triangle['triangle']=output
    return triangle
"""