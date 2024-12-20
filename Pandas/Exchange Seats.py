"""
626. Exchange Seats
Solved
Medium
Topics
Companies
SQL Schema
Pandas Schema
Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
id is a continuous increment.

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

The result format is in the following example.

Example 1:

Input:
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
Output:
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
Explanation:
Note that if the number of students is odd, there is no need to change the last one's seat.
"""

import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    def swap_rows(df, row1, row2):
        df.iloc[row1], df.iloc[row2] =  df.iloc[row2].copy(), df.iloc[row1].copy()
        return df
    i = 0
    while i < len(seat):
        if i+1 < len(seat):
            swap_rows(seat, i, i+1)
        i += 2
    seat['id'] = range(1, len(seat)+1)
    return seat

"""
import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    id = list(range(1, len(seat)+1))
    for i in range(1, len(id), 2):
        id[i-1], id[i] = id[i], id[i-1]
        seat['id'] = id
    return seat.sort_values(by='id')
"""