"""
176. Second Highest Salary
Solved
Medium
Topics
Companies
SQL Schema
Pandas Schema
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.


Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

Example 1:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
8%
"""

import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('salary').count().reset_index()
    if len(df['salary']) == 1:
        df.loc[0, 'salary'] = np.nan
    else:
        df.drop(df['salary'].idxmax(), axis=0, inplace=True)
    return pd.DataFrame({"SecondHighestSalary" : [df.salary.max(skipna=False)]})

"""
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
        Unique =  employee["salary"].sort_values(ascending = False).drop_duplicates()
        if len(Unique) < 2:
            return pd.DataFrame({"SecondHighestSalary":[None]})
        else :
            return pd.DataFrame({"SecondHighestSalary":[Unique.iloc[1]]}) 
"""