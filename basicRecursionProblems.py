# my implementations of 27 basic recursive algorithms
# These problems were non-graded practice problems in my CS-313E class -
# hence I am posting my solutions

# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies 
# recursively (without loops or multiplication).
def bunnyEars(bunnies):
    if bunnies < 1:
        return 0
    elif bunnies == 1:
        return 2
    else:
        return 2 + bunnyEars(bunnies - 1)

# We have bunnies standing in a line, numbered 1, 2, ...
# The odd bunnies (1, 3, ..) have the normal 2 ears.
# The even bunnies (2, 4, ..) we'll say have 3 ears, because they each 
# have a raised foot. Recursively return the number of "ears" in the 
# bunny line 1, 2, ... n (without loops or multiplication).
def bunnyEars2(bunnies):
    if bunnies < 1:
        return 0
    elif bunnies == 1:
        return 2
    elif bunnies % 2 == 0:
        return 3 + bunnyEars2(bunnies - 1)
    elif bunnies % 2 == 1:
        return 2 + bunnyEars2(bunnies - 1)

# We have triangle made of blocks. The topmost row has 1 block, the 
# next row down has 2 blocks, the next row has 3 blocks, and so on.
# Compute recursively (no loops or multiplication) the total number of 
# blocks in such a triangle with the given number of rows. 
def triangle(rows):
    if rows == 0:
        return 0
    elif rows == 1:
        return 1
    else:
        return rows + triangle(rows - 1)

# Given a non-negative int n, return the sum of its digits recursively 
# (no loops). Note that mod (%) by 10 yields the rightmost digit 
# (126 % 10 is 6), while divide (//) by 10 removes the rightmost digit 
# (126 // 10 is 12).
def sumDigits(n):
    if len(str(n)) < 1:
        return 0
    elif len(str(n)) == 1:
        return n
    else:
        return n % 10 + sumDigits(n // 10)

# Given a non-negative int n, return the count of the occurrences of 7 
# as a digit, so for example 717 yields 2. (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), 
# while divide (//) by 10 removes the rightmost digit (126 // 10 is 12).
def count7(n):
    if len(str(n)) == 0:
        return 0
    elif len(str(n)) == 1:
        if n == 7:
            return 1
        else:
            return 0
    elif n % 10 == 7:
        return 1 + count7(n // 10)
    else:
        return count7(n // 10)


# Given a non-negative int n, compute recursively (no loops) the count 
# of the occurrences of 8 as a digit, except that an 8 with
# another 8 immediately to its left counts double, so 8818 yields 4. 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (//) by 10 removes the rightmost digit (126 // 10 is 12).
def count8(n):
    if len(str(n)) == 0:
        return 0
    elif len(str(n)) == 1:
        if n == 8:
            return 1
        else:
            return 0
    elif n % 10 == 8:
        if (n // 10) % 10 == 8:
            return 2 + count8(n // 10)
        else:
            return 1 + count8(n // 10)
    else:
        return count8(n // 10)

# Given base and n that are both 1 or more, compute recursively (no loops) 
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
def powerN(base, n):
    if n == 0:
        return 1
    elif n == 1:
        return base
    else:
        return base * powerN(base, n - 1)

# Given a string, compute recursively (no loops) the number of lowercase 
# 'x' chars in the string.
def countX(str):
    if len(str) < 2:
        if str == 'x':
            return 1
        else:
            return 0
    elif str[0] == 'x':
        return 1 + countX(str[1:])
    else:
        return countX(str[1:])

# Given a string, compute recursively (no loops) the number of times 
# lowercase "hi" appears in the string.
def countHi(str):
    if len(str) < 3:
        if str == 'hi':
            return 1
        else:
            return 0
    else:
        if str[0:2] == 'hi':
            return 1 + countHi(str[1:])
        else:
            return countHi(str[1:])


# Given a string, compute recursively (no loops) a new string where all 
# the lowercase 'x' chars have been changed to 'y' chars. 
def changeXY(str):
    if len(str) < 1:
        return ''
    elif len(str) == 1:
        if str == 'x':
            return 'y'
        else:
            return str
    else:
        if str[0] == 'x':
            return 'y' + changeXY(str[1:])
        else:
            return str[0] + changeXY(str[1:])
    
      

# Given a string, compute recursively (no loops) a new string where all 
# appearances of "pi" have been replaced by "3.14".
def changePi(str):
    if len(str) < 1:
        return ""
    elif len(str) == 1:
        return str
    elif len(str) == 2:
        if str == 'pi':
            return '3.14'
        else:
            return str
    else:
        if str[0:2] == 'pi':
            return '3.14' + changePi(str[2:])
        else:
            return str[0:1] +  changePi(str[1:])

# Given a string, compute recursively a new string where all the 'x' 
# chars have been removed.
def noX(str):
    if len(str) < 1:
        return ""
    elif len(str) == 1:
        if str == 'x':
            return ""
        else:
            return str
    else:
        if str[0] == 'x':
            return noX(str[1:])
        else:
            return str[0] + noX(str[1:])


# Given an array of ints, compute recursively if the array contains a 6.
# We'll use the convention of considering only the part of the array that 
# begins at the given index. In this way, a recursive call can pass index+1 
# to move down the array. The initial call will pass in index as 0.
def array6(nums, index):
    if len(nums) < 1:
        return False
    elif index == len(nums) - 1:
        return nums[index] == 6
    else:
        if nums[index] == 6:
            return True
        else:
            return array6(nums, index + 1)


# Given an array of ints, compute recursively the number of times that the 
# value 11 appears in the array. We'll use the convention of considering 
# only the part of the array that begins at the given index. In this way, 
# a recursive call can pass index+1 to move down the array. The initial 
# call will pass in index as 0. 
def array11(nums, index):
    if len(nums) < 1:
        return 0
    elif index == len(nums) - 1:
        if nums[index] == 11:
            return 1
        else:
            return 0
    else:
        if nums[index] == 11:
            return 1 + array11(nums, index + 1)
        else:
            return array11(nums, index + 1)


# Given an array of ints, compute recursively if the array contains 
# somewhere a value followed in the array by that value times 10. We'll 
# use the convention of considering only the part of the array that begins 
# at the given index. In this way, a recursive call can pass index+1 to 
# move down the array. The initial call will pass in index as 0.
def array220(nums, index):
    if index > len(nums) - 2:
        return False
    elif index == len(nums) - 2:
        return nums[index + 1] == nums[index] * 10
    else:
        if (nums[index] * 10) in nums[index:]:
            return True
        else:
            return array220(nums, index + 1)



# Given a string, compute recursively a new string where all the adjacent 
# chars are now separated by a "*".
def allStar(str):
    if len(str) < 1:
        return ""
    elif len(str) == 1:
        return str
    else:
        return str[0] + '*' + allStar(str[1:])



# Given a string, compute recursively a new string where identical chars 
# that are adjacent in the original string are separated from each other 
# by a "*".
def pairStar(str):
    if len(str) < 2:
        return str
    elif len(str) == 2:
        if str[0] == str[1]:
            return str[0] + '*' + str[1]
        else:
            return str
    else:
        if str[0] == str[1]:
            return str[0] + '*' + pairStar(str[1:])
        else:
            return str[0] + pairStar(str[1:])


# Given a string, compute recursively a new string where all the lowercase 
# 'x' chars have been moved to the end of the string.
def endX(str):
    if len(str) < 2:
        return str
    elif len(str) == 2:
        if str[0] == 'x':
            return str[1] + str[0]
        else:
            return str
    else:
        if str[0] == 'x':
            return endX(str[1:]) + 'x'
        else:
            return str[0] + endX(str[1:])



# We'll say that a "pair" in a string is two instances of a char separated 
# by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" 
# contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number 
# of pairs in the given string.
def countPairs(str):
    if len(str) < 3:
        return 0
    elif len(str) == 3:
        if str[0] == str[2]:
            return 1
        else:
            return 0
    else:
        if str[0] == str[2]:
            return 1 + countPairs(str[1:])
        else:
            return countPairs(str[1:])



# Count recursively the total number of "abc" and "aba" substrings that 
# appear in the given string.
def countAbc(str):
    if len(str) < 3:
        return 0
    elif len(str) == 3:
        if str == 'abc' or str == 'aba':
            return 1
        else:
            return 0
    else:
        if str[:3] == 'abc' or str[:3] == 'aba':
            return 1 + countAbc(str[1:])
        else:
            return countAbc(str[1:])


# Given a string, compute recursively (no loops) the number of "11" 
# substrings in the string. The "11" substrings should not overlap.
def count11(str):
    if len(str) < 2:
        return 0
    elif len(str) == 2:
        if str == '11':
            return 1
        else:
            return 0
    else:
        if str[:2] == '11':
            return 1 + count11(str[2:])
        else:
            return count11(str[1:])


# Given a string, return recursively a "cleaned" string where adjacent 
# chars that are the same have been reduced to a single char. So "yyzzza" 
# yields "yza".
def stringClean(str):
    if len(str) < 1:
        return ''
    elif len(str) == 1:
        return str
    else:
        if str[0] == str[1]:
            return stringClean(str[1:])
        else:
            return str[0] + stringClean(str[1:])


# Given a string, compute recursively the number of times lowercase "hi" 
# appears in the string, however do not count "hi" that have an 'x' 
# immedately before them.
def countHi2(str):
    if len(str) < 2:
        return 0
    elif str == 'xhi':
        return 0
    elif str == 'hi':
        return 1
    elif len(str) < 3:
        return 0
    else:
        if str[0:3] == 'xhi':
            return countHi2(str[3:])
        elif str[:2] == 'hi':
            return 1 + countHi2(str[2:])
        else:
            return countHi2(str[1:])



# Given a string that contains a single pair of parenthesis, compute 
# recursively a new string made of only of the parenthesis and their 
# contents, so "xyz(abc)123" yields "(abc)".
def parenBit(str):
    if str[0] == '(' and str[len(str) - 1] == ')':
        return str
    elif str[0] == '(':
        return parenBit(str[:len(str) - 1])
    else:
        return parenBit(str[1:])


# Given a string, return True if it is a nesting of zero or more pairs 
# of parenthesis, like "(())" or "((()))". Suggestion: check the first 
# and last chars, and then recur on what's inside them.
def nestParen(str):
    if len(str) < 1:
        return True
    elif len(str) % 2 != 0:
        return False
    elif len(str) == 2:
        if str[0] == '(' and str[1] == ')':
            return True
        else:
            return False
    elif not (str[0] == '(' and str[len(str) - 1] == ')'):
        return False
    else:
        return nestParen(str[1:len(str) - 1])


# Given a string and a non-empty substring sub, compute recursively the 
# number of times that sub appears in the string, without the sub strings 
# overlapping.
def strCount(str, sub):
    if len(str) < len(sub):
        return 0
    elif len(str) == len(sub):
        if str == sub:
            return 1
        else:
            return 0
    elif str[:len(sub)] == sub:
        return 1 + strCount(str[len(sub):], sub)
    else:
        return strCount(str[1:], sub)


# Given a string and a non-empty substring sub, compute recursively if 
# at least n copies of sub appear in the string somewere, possibly with 
# overlapping. n will be non-negative.
def strCopies(str, sub, n):
    if n == 0:
        return True
    elif len(str) < len(sub):
        return n == 0
    elif len(str) == len(sub):
        if str == sub:
            n -= 1
        return n == 0
    elif str[:len(sub)] == sub:
        return strCopies(str[1:], sub, n - 1)
    else:
        return strCopies(str[1:], sub, n)
