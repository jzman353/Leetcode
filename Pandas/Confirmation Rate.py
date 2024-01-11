"""
1934. Confirmation Rate
Solved
Medium
Topics
Companies
SQL Schema
Pandas Schema
Table: Signups

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
user_id is the column of unique values for this table.
Each row contains information about the signup time for the user with ID user_id.

Table: Confirmations

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
| action         | ENUM     |
+----------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
user_id is a foreign key (reference column) to the Signups table.
action is an ENUM (category) of the type ('confirmed', 'timeout')
Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').

The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

Write a solution to find the confirmation rate of each user.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input:
Signups table:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |
+---------+---------------------+
Confirmations table:
+---------+---------------------+-----------+
| user_id | time_stamp          | action    |
+---------+---------------------+-----------+
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-02-28 23:59:59 | timeout   |
+---------+---------------------+-----------+
Output:
+---------+-------------------+
| user_id | confirmation_rate |
+---------+-------------------+
| 6       | 0.00              |
| 3       | 0.00              |
| 7       | 1.00              |
| 2       | 0.50              |
+---------+-------------------+
Explanation:
User 6 did not request any confirmation messages. The confirmation rate is 0.
User 3 made 2 requests and both timed out. The confirmation rate is 0.
User 7 made 3 requests and all were confirmed. The confirmation rate is 1.
User 2 made 2 requests where one was confirmed and the other timed out. The confirmation rate is 1 / 2 = 0.5.

#71%
"""

import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(signups, confirmations, how='outer', on='user_id')[['user_id', 'action']]
    df['action']=df['action'].map(lambda x : 1 if x=='confirmed' else 0)
    df=df.groupby(['user_id'])['action'].mean().round(2).reset_index()
    df.rename(columns={"action":"confirmation_rate"}, inplace=True)
    return df

"""
import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    
    confirmed = {}
    total = {}
    for i in signups.index:
        confirmed[signups["user_id"][i]] = 0.0
        total[signups["user_id"][i]] = 0.0

    for i in confirmations.index:
        total[confirmations["user_id"][i]] += 1
        if confirmations["action"][i] == "confirmed":
            confirmed[confirmations["user_id"][i]] += 1

    col1 = []
    col2 = []
    for user_id in total:
        col1.append(user_id)
        if total[user_id] == 0:
            confirmation_rate = 0
        else:
            confirmation_rate = confirmed[user_id] / total[user_id]
            confirmation_rate = round(confirmation_rate, 2)
        col2.append(confirmation_rate)

    ans = {"user_id" : col1, "confirmation_rate" : col2}

    ans = pd.DataFrame(ans)

    return ans
"""