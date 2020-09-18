#72%
#Runtime: 36 ms
#Memory Usage: 14.1 MB

'''
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.



Example 1:

Input: A = [1,2,3,4]
Output: "23:41"

Example 2:

Input: A = [5,5,5,5]
Output: ""

Example 3:

Input: A = [0,0,0,0]
Output: "00:00"

Example 4:

Input: A = [0,0,1,0]
Output: "10:00"



Constraints:

    arr.length == 4
    0 <= arr[i] <= 9


'''

def largestTimeFromDigits(arr) -> str:
    copy = arr
    count4 = 0
    # Not Possible:
    # 31:10, 31:60, 33:33
    # Case 1 failure - there are too many end digits where digit1 is 0 or 1
    if arr.count(6) + arr.count(7) + arr.count(8) + arr.count(9) > 2:
        return ""
    # Case 3 failure - there not enought digits that can fit in digit1
    if arr.count(0) + arr.count(1) + arr.count(2) < 1:
        return ""

    # First digit is 2
    if 2 in copy and (0 in copy or 1 in copy or copy.count(2) > 1 or 3 in copy) and copy.count(6)+copy.count(7)+copy.count(8)+copy.count(9) <= 1:
        digit1 = 2
        copy.remove(2)
        digit2 = 3 if 3 in arr else 2 if 2 in arr else 1 if 1 in arr else 0
        copy.remove(digit2)
        if 6 in copy or 7 in copy or 8 in copy or 9 in copy:
            digit4 = 6 if 6 in copy else 7 if 7 in copy else 8 if 8 in copy else 9 if 9 in copy else max(copy)
            copy.remove(digit4)
            # Case 2 failure - there are too many end digits where digit1 is 2
            if copy[0] >= 6:
                return ""
            else:
                digit3 = copy[0]
        else:
            digit3 = max(copy)
            digit4 = min(copy)
        return str(digit1) + str(digit2) + ":" + str(digit3) + str(digit4)

    # First digit is 1
    elif 1 in copy:
        digit1 = 1
        copy.remove(1)
        digit2 = max(copy)
        copy.remove(digit2)
        if 6 in copy or 7 in copy or 8 in copy or 9 in copy:
            digit4 = 6 if 6 in copy else 7 if 7 in copy else 8 if 8 in copy else 9 if 9 in copy else max(copy)
            copy.remove(digit4)
            # Case 2 failure - there are too many end digits where digit1 is 2
            if copy[0] >= 6:
                return ""
            else:
                digit3 = copy[0]
        else:
            digit3 = max(copy)
            digit4 = min(copy)
        return str(digit1) + str(digit2) + ":" + str(digit3) + str(digit4)

    # First digit is 0
    elif 0 in copy:
        digit1 = 0
        copy.remove(0)
        digit2 = max(copy)
        copy.remove(digit2)
        if 6 in copy or 7 in copy or 8 in copy or 9 in copy:
            digit4 = 6 if 6 in copy else 7 if 7 in copy else 8 if 8 in copy else 9 if 9 in copy else max(copy)
            copy.remove(digit4)
            # Case 2 failure - there are too many end digits where digit1 is 2
            if copy[0] >= 6:
                return ""
            else:
                digit3 = copy[0]
        else:
            digit3 = max(copy)
            digit4 = min(copy)
        return str(digit1) + str(digit2) + ":" + str(digit3) + str(digit4)
    else:
        return ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #arr=[1,2,3,4]
    #arr = [1, 9, 6, 0]
    #arr = [3, 2, 7, 0]
    arr = [2,0,6,6] #169/172
    print(largestTimeFromDigits(arr))

'''
def largestTimeFromDigits(self, A: List[int]) -> str:
        
        max_time = -1

        for h1, h2, m1, m2 in itertools.permutations(A):

            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2

            if hours <24 and minutes < 60:

                max_time = max(hours * 60 + minutes, max_time)

        if max_time == -1: return ""

        return  "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
'''