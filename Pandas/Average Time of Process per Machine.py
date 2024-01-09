"""
1661. Average Time of Process per Machine
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Activity

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
The table shows the user activities for a factory website.
(machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
machine_id is the ID of a machine.
process_id is the ID of a process running on the machine with ID machine_id.
activity_type is an ENUM (category) of type ('start', 'end').
timestamp is a float representing the current time in seconds.
'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.

There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.

The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input:
Activity table:
+------------+------------+---------------+-----------+
| machine_id | process_id | activity_type | timestamp |
+------------+------------+---------------+-----------+
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
| 1          | 1          | start         | 0.430     |
| 1          | 1          | end           | 1.420     |
| 2          | 0          | start         | 4.100     |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.500     |
| 2          | 1          | end           | 5.000     |
+------------+------------+---------------+-----------+
Output:
+------------+-----------------+
| machine_id | processing_time |
+------------+-----------------+
| 0          | 0.894           |
| 1          | 0.995           |
| 2          | 1.456           |
+------------+-----------------+
Explanation:
There are 3 machines running 2 processes each.
Machine 0's average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
Machine 1's average time is ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
Machine 2's average time is ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456

#23%
"""

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # Define a function to multiply timestamp by -1 if activity_type is start
    def multiply_time(row):
        if row['activity_type'] == 'start':
            return -row['timestamp']
        else:
            return row['timestamp']

    # Apply the function to the timestamp column and assign the result to replace the timestamp column data
    activity['timestamp'] = activity.apply(multiply_time, axis=1)

    # Count unique processes per machine id and sum all times (with start times being negative)
    df = activity.groupby('machine_id', as_index=False).agg(process_count=('process_id', 'nunique'), timestamp=('timestamp', 'sum'))

    # Calculate processing_time
    df['processing_time'] = (df['timestamp']/df['process_count']).round(3)

    # Only return columns machine_id and processing_time
    return df[['machine_id', 'processing_time']]

"""
import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
   df1 = activity[activity['activity_type'] == 'start']
   df2 = activity[activity['activity_type'] == 'end']
   df = pd.merge(df1,df2, on=['machine_id','process_id'])
   df['processing_time'] = df['timestamp_y'] - df['timestamp_x']
   result = df.groupby('machine_id')[['processing_time']].mean().round(3).reset_index()
   return result
   
import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity['timestamp'] = activity.apply(lambda x: x.timestamp * -1 if x.activity_type == 'start' else x.timestamp, axis=1)
    sum_machine_process = activity.groupby(['machine_id', 'process_id'], as_index=False)['timestamp'].sum()
    mean_machine = sum_machine_process.groupby(['machine_id'], as_index=False)['timestamp'].mean().round(3).rename(columns = {'timestamp': 'processing_time'})
    return mean_machine
"""