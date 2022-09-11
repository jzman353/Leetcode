"""
Imagine an array that contains both integers and nested arrays, such as the following: [8, 4, [5, [9], 3], 6].
The depth sum is described as the weighted sum of each integer, weighted by their respective depths.
In the example, 8's depth is 1, while 9's is 3.
Given such an array, calculate its depth sum.

For example:
Input: [4, [5, 6]]
Output: 4 + 2 * 5 + 2 * 6 = 26
Input: [8, 4, [5, [9], 3], 6]
Output: 8 + 4 + 2 * 5 + 3 * 9 + 2 * 3 + 6 = 61
"""
class depth_question:
	def __init__(self):
		self.answer = 0

	def sum_depth(self, arr, weight = 1):
		idx = 0
		print(arr)
		while idx < len(arr):
			print(arr[idx])
			if isinstance(arr[idx], list):
				self.sum_depth(arr[idx], weight + 1)
			else:
				self.answer += weight * arr[idx]
			idx += 1
		return self.answer

if __name__ == '__main__':
	d = depth_question()
	print(d.sum_depth([4, [5, 6]]))

"""
Balance Parentheses

Given a string with alpha-numeric characters and parentheses, return a string with balanced parentheses by removing the fewest characters 
possible. You cannot add anything to the string.
Balanced parentheses means that each opening parenthesis has a corresponding closing parenthesis and the pairs of parentheses are 
properly nested.

balance("()") -> "()"
balance("a(b)c)") -> "a(b)c"
balance(")(") -> ""
balance("(((((") -> ""
balance("(()()(") -> "()()"
balance(")(())(") -> "(())"
balance(")())(()()(") -> "()()()" 

There can be multiple correct results per input

balance("a(b)c)") -> "a(b)c" or "a(bc)"
balance("(())())") -> "(()())" or "(())()"

def remove_parenthesis(s):
	l = 0
	r = 0
	remove = []

	for i in range(len(s)):
		if s[i] == '(':
			l += 1
		elif s[i] == ')':
			r += 1
		if r > l:
			remove.append(i)
			r -= 1

	l = 0
	r = 0
	for i in range(len(s)-1,-1,-1):
		if s[i] == '(':
			l += 1
		elif s[i] == ')':
			r += 1
		if l > r:
			remove.append(i)
			l -= 1

	list_s = list(s)
	final = []
	for i in range(len(list_s)):
		if i not in remove:
			final.append(list_s[i])

	return ''.join(final)

print(remove_parenthesis("(())())"))
"""