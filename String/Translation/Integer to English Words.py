"""
273. Integer to English Words
Hard

Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

Constraints:

    0 <= num <= 231 - 1
"""
#88%
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        rules = {
            #1000000000000000000000000000000000:"Decillion",
            #1000000000000000000000000000000:"Nonillion",
            #1000000000000000000000000000:"Octillion",
            #1000000000000000000000000:"Septillion",
            #1000000000000000000000:"Sextillion",
            #1000000000000000000:"Quintillion",
            #1000000000000000:"Quadrillion",
            #1000000000000:"Trillion",
            1000000000:"Billion",
            1000000:"Million",
            1000:"Thousand",
            100:"Hundred",
            90:"Ninety",
            80:"Eighty",
            70:"Seventy",
            60:"Sixty",
            50:"Fifty",
            40:"Forty",
            30:"Thirty",
            20:"Twenty",
            19:"Nineteen",
            18:"Eighteen",
            17:"Seventeen",
            16:"Sixteen",
            15:"Fifteen",
            14:"Fourteen",
            13:"Thirteen",
            12:"Twelve",
            11:"Eleven",
            10:"Ten",
            9:"Nine",
            8:"Eight",
            7:"Seven",
            6:"Six",
            5:"Five",
            4:"Four",
            3:"Three",
            2:"Two",
            1:"One",
        }

        ans = ""
        for value, word in rules.items():
            while num >= value:
                if num == value and value < 100:
                    ans += " " + rules[value]
                    num -= value
                    break
                else:
                    temp = str(num // value) if num >= 1000 else str(num)
                    if len(temp) == 2:
                        temp = "0"+temp
                    elif len(temp) == 1:
                        temp = "00" + temp

                    if len(temp) == 3:
                        if temp[0] == "0":
                            hundreds = ""
                        else:
                            hundreds = rules[int(temp[0])] + " " + rules[100]
                        teens = False
                        if temp[1] == "0":
                            tens = ""
                        elif temp[1] == "1":
                            teens = True
                            tens = rules[int(temp[1]+temp[2])]
                        else:
                            tens = rules[int(temp[1])*10]
                        if temp[2] == "0":
                            ones = ""
                        else:
                            ones = rules[int(temp[2])]
                        if num > 999:
                            if teens:
                                ans += hundreds + " " + tens + " " + word + " "
                            else:
                                ans += hundreds + " " + tens + " " + ones + " " + word + " "
                        else:
                            if teens:
                                ans += hundreds + " " + tens
                            else:
                                ans += hundreds + " " + tens + " " + ones
                    num -= value*int(temp)
        ans = " ".join([i for i in ans.split(" ") if i != ""])
        return ans

if __name__ == '__main__':
    def test(input1):
        Test = Solution()
        ans = Test.numberToWords(input1)
        print(ans)
        return ans


    assert test(0) == "Zero"
    assert test(1) == "One"
    assert test(11) == "Eleven"
    assert test(12) == "Twelve"
    assert test(18) == "Eighteen"
    assert test(24) == "Twenty Four"
    assert test(99) == "Ninety Nine"
    assert test(123) == "One Hundred Twenty Three"
    assert test(1000) == "One Thousand"
    assert test(12001) == "Twelve Thousand One"
    assert test(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert test(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    assert test(1234567891) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    assert test(12000111) == "Twelve Million One Hundred Eleven"

"""
class Solution:
    def numberToWords(self, num: int) -> str:
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)
        
        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)
        

        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tenner = num // 10
                rest = num - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)
        
        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest) 
            elif not hundred and rest: 
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'
        
        billion = num // 1000000000
        million = (num%1000000000) // 1000000
        thousand = (num%1000000) // 1000
        rest = num%1000
        
        if not num:
            return 'Zero'
        
        result = ''
        if billion:        
            result = three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''    
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result
"""