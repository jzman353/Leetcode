import math
def smallest_subarray(input,S):
    summ = 0
    head = 0
    ans = math.inf
    for i in range(len(input)):
        summ += input[i]
        while summ >= S:
            ans = min(ans,i-head+1)
            summ -= input[head]
            head += 1
    if ans == math.inf:
        return 0
    return ans

if __name__ == '__main__':
    def test(input1, input2):
        ans = smallest_subarray(input1,input2)
        print(ans)
        return ans
    assert test([2, 1, 5, 2, 3, 2], 7) == 2
    assert test([2, 1, 5, 2, 8], 7) == 1
    assert test([3, 4, 1, 1, 6], 8) == 3
    assert test([3, 4, 8, 1, 6], 8) == 1
    assert test([8, 4, 1, 1, 6], 8) == 1
    assert test([8, 4, 1, 1, 6], 21) == 0