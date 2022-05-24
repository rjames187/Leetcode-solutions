class Solution:
    def isValid(self, s: str) -> bool:

        
        key = {'(' : ')', '[' : ']', '{' : '}'}
        
        stack = []
        
        for i in s:
            if i in key:
                stack.insert(0, i)
            elif len(stack) == 0:
                return False
            elif i != key[stack[0]]:
                return False
            else:
                stack.pop(0)
        
        if len(stack) != 0:
            return False
        return True
                