"""
937. Reorder Data in Log Files
Easy

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

Constraints:

1 <= logs.length <= 100
3 <= logs[i].length <= 100
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.
"""
#22%
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l = {}
        d = []
        for i in logs:
            temp = i.split()
            if temp[-1][0] in string.ascii_letters:
                if temp[0] not in l.keys():
                    l[temp[0]] = " ".join(temp[1:])
                else:
                    l[temp[0]+"-"] = " ".join(temp[1:])
            else:
                d.append(i)
        answer = []
        for i,val in sorted(l.items(), key=lambda x: (x[1],x[0])):
            if i[-1] != "-":
                answer.append(i+" "+val)
            else:
                answer.append(i[:-1]+" "+val)
        for i in d:
            answer.append(i)
        return answer

"""
Approach 2: Sorting by Keys
Intuition

Rather than defining pairwise relationships among all elements in a collection, the order of the elements can also be defined with sorting keys.

To illustrate the idea, let us first define a Student object as follows, which has three properties: name, grade, age.

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
Now, if we are asked to sort the list of students by age in ascending order, we could simply use the age property of each student as the sorting key, as follows:

>>> sorted(student_objects, key=lambda student: student.age)
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
Furthermore, the key could be a tuple of multiple keys, i.e. tuple(key_1, key_2, ... key_n).

If two elements have the same value on key_1, the comparison will carry on for the following keys, i.e. key_2 ... key_n.

As a result, if we are asked to sort the students first by the grade, then by the age, we can simply return the compound key (stduent.grade, student.age), as follows:

>>> sorted(student_objects, key=lambda student: (student.grade, student.age))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
Algorithm

Given the above intuition, it should be clear that all we need is to translate the rules we defined before into a tuple of keys.

As a reminder, here are a list of the rules that we defined before, concerning the order of logs:

1). The letter-logs should be prioritized above all digit-logs.

2). Among the letter-logs, we should further sort them based on firstly on their contents, and then on their identifiers if the contents are identical.

3). Among the digit-logs, they should remain in the same order as they are in the collection.

To ensure the above order, we could define a tuple of 3 keys, (key_1, key_2, key_3), as follows:

key_1: this key serves as a indicator for the type of logs. For the letter-logs, we could assign its key_1 with 0, and for the digit-logs, we assign its key_1 with 1. As we can see, thanks to the assigned values, the letter-logs would take the priority above the digit-logs.

key_2: for this key, we use the content of the letter-logs as its value, so that among the letter-logs, they would be further ordered based on their content, as required in the Rule (2).

key_3: similarly with the key_2, this key serves to further order the letter-logs. We will use the identifier of the letter-logs as its value, so that for the letter-logs with the same content, we could further sort the logs based on its identifier, as required in the Rule (2).

Note: for the digit-logs, we don't need the key_2 and key_3. We can simply assign the None value to these two keys. As a result, the key value for all the digit-logs would be (1, None, None).

Finally, thanks to the stability of sorting algorithms, the elements with the same key value would remain the same order as in the original input. Therefore, the Rule (3) is ensured.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)

Complexity Analysis

Let NN be the number of logs in the list and MM be the maximum length of a single log.

Time Complexity: \mathcal{O}(M \cdot N \cdot \log N)O(M⋅N⋅logN)

The sorted() in Python is implemented with the Timsort algorithm whose time complexity is \mathcal{O}(N \cdot \log N)O(N⋅logN).

Since the keys of the elements are basically the logs itself, the comparison between two keys can take up to \mathcal{O}(M)O(M) time.

Therefore, the overall time complexity of the algorithm is \mathcal{O}(M \cdot N \cdot \log N)O(M⋅N⋅logN).

Space Complexity: \mathcal{O}(M \cdot N)O(M⋅N)

First, we need \mathcal{O}(M \cdot N)O(M⋅N) space to keep the keys for the log.

In addition, the worst space complexity of the Timsort algorithm is \mathcal{O}(N)O(N), assuming that the space for each element is \mathcal{O}(1)O(1). Hence we would need \mathcal{O}(M \cdot N)O(M⋅N) space to hold the intermediate values for sorting.

In total, the overall space complexity of the algorithm is \mathcal{O}(M \cdot N + M \cdot N) = \mathcal{O}(M \cdot N)O(M⋅N+M⋅N)=O(M⋅N).
"""