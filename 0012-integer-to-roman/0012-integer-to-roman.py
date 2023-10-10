from math import ceil

class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = {
            0: ('I', 'V'),
            1: ('X', 'L'),
            2: ('C', 'D'),
            3: ('M', 'error')
        }
        res = ''
        num = str(num)
        for i in range(len(num)):
            digit = num[-1 * (i + 1)]
            if digit in ('1', '2', '3'):
                res = (numerals[i][0] * int(digit)) + res
            elif digit == '4':
                res = numerals[i][0] + numerals[i][1] + res
            elif digit == '5':
                res = numerals[i][1] + res
            elif digit in ('6', '7', '8'):
                res = numerals[i][1] + (numerals[i][0] * (int(digit) - 5)) + res
            elif digit == '9':
                res = numerals[i][0] + numerals[i + 1][0] + res
            
        return res
                