'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.

Runtime: 36 ms Beats 12%
Memory Usage: 13.9 MB
'''

class Solution:
    def defangIPaddr(self, address: str) -> str:
        Dummy_Address=[]
        for i in range(len(address)):
            Dummy_Address=address.replace(".", "[.]")
        return Dummy_Address

'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
'''