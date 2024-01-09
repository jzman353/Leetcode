"""
1789. Primary Department for Each Employee
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Employee

+---------------+---------+
| Column Name   |  Type   |
+---------------+---------+
| employee_id   | int     |
| department_id | int     |
| primary_flag  | varchar |
+---------------+---------+
(employee_id, department_id) is the primary key (combination of columns with unique values) for this table.
employee_id is the id of the employee.
department_id is the id of the department to which the employee belongs.
primary_flag is an ENUM (category) of type ('Y', 'N'). If the flag is 'Y', the department is the primary department for the employee. If the flag is 'N', the department is not the primary.

Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is 'N'.

Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input:
Employee table:
+-------------+---------------+--------------+
| employee_id | department_id | primary_flag |
+-------------+---------------+--------------+
| 1           | 1             | N            |
| 2           | 1             | Y            |
| 2           | 2             | N            |
| 3           | 3             | N            |
| 4           | 2             | N            |
| 4           | 3             | Y            |
| 4           | 4             | N            |
+-------------+---------------+--------------+
Output:
+-------------+---------------+
| employee_id | department_id |
+-------------+---------------+
| 1           | 1             |
| 2           | 1             |
| 3           | 3             |
| 4           | 3             |
+-------------+---------------+
Explanation:
- The Primary department for employee 1 is 1.
- The Primary department for employee 2 is 1.
- The Primary department for employee 3 is 3.
- The Primary department for employee 4 is 3.

9%
"""

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    df_multiple = employee[employee['primary_flag']=='Y'][['employee_id', 'department_id']]
    df_one = employee.groupby('employee_id')['department_id'].count().reset_index()
    df_one = df_one[df_one['department_id'] == 1]
    df_one_correct = pd.merge(df_one, employee, on=['employee_id'], how='left')[['employee_id', 'department_id_y']]
    df_one_correct.rename(columns={"department_id_y":"department_id"}, inplace=True)
    return pd.merge(df_multiple, df_one_correct, on=['employee_id', 'department_id'], how='outer')

"""
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:

    primary = {}
    count = {}
    first = {}
    for i in employee.index:
        employee_id = employee["employee_id"][i]
        department_id = employee["department_id"][i]
        primary_flag = employee["primary_flag"][i]
        if primary_flag == "Y":
            primary[employee_id] = department_id
        if employee_id in count:
            count[employee_id] += 1
        else:
            count[employee_id] = 1
            first[employee_id] = department_id
    
    col1 = []
    col2 = []
    for employee_id in count:
        if count[employee_id] == 1:
            col1.append(employee_id)
            col2.append(first[employee_id])
        else:
            if employee_id in primary:
                col1.append(employee_id)
                col2.append(primary[employee_id])

    ans = {"employee_id" : col1, "department_id" : col2}

    ans = pd.DataFrame(ans)

    return ans
"""