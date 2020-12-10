"""
Given two list of the same length and a expected result, write a function that calculates the result from one number in each list.. You are NOT allowed to use two numbers from the same list.
Bronze Return any two numbers that multiply to that result
Silver Return all two number pairs that multiply to that result
Gold If the result is not possible, return the closest possible result (ie if need 23, and can make 22, return 22)
"""

from itertools import product
def findit(in1, in2, exp):
    return [ (x,y) for (x,y) in product(in1, in2) if x*y == exp]

"""
def findit(in1, in2, exp):
    tolerance = 500
    result = []
    for i in in1:
        for j in in2:
            if (i*j == exp):
                result.append((i,j))
            else:
                new_tolerance = abs((i*j) - exp)
                if (new_tolerance < tolerance):
                    tolerance = new_tolerance
                    nearest = (i,j)

    if len(result) == 0:
        return nearest
    else:
        return result

#I went for a divide and conquer approach, till i got a single match:
def findit_faster_times(in1, in2, exp):
    in1 = sorted(in1)   #Arrange smallest to lowest
    in2 = sorted(in2)   #Arrange smallest to lowest
    gap_from_goal = in1[0] * in2[0] - exp   #Find out the biggest gap to needed
    list_len = len(in2)-1   #This is used as a referene in the while loop
    low_index = 0           #set a low point to cound up the list from
    high_index = len(in2)-1 #set a max igh point to count down the list (-1 as index starts at 0)
    while low_index < list_len or high_index > 0:  #Keep running till we end a list
        result = in1[low_index] * in2[high_index]
        new_gap_from_goal = result - exp
        if new_gap_from_goal == 0:
            return f'{in1[low_index]} + {in2[high_index]} = {exp}'
        if new_gap_from_goal > gap_from_goal:
            high_index -= 1
        else:
            low_index += 1
"""