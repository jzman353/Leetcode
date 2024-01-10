"""
180. Consecutive Numbers
Solved
Medium
Topics
Companies
SQL Schema
Pandas Schema
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column.

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input:
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
21%
"""

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    l = logs['num']
    s = set()
    for i in range(len(l)-2):
        if l[i] not in s and l[i] == l[i+1] == l[i+2]:
            s.add(l[i])
    return pd.DataFrame({"ConsecutiveNums":list(s)})

"""
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    current_num = None
    count = 0
    consecutive_nums=[]

    for i in logs['num']:
        if i == current_num:
            count += 1
        else:
            current_num = i
            count = 1
        
        if count >= 3 and i not in consecutive_nums:
            consecutive_nums.append(i)
    return pd.DataFrame({'ConsecutiveNums':consecutive_nums})
"""