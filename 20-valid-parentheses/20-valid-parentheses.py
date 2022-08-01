class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', ']': '[', '}': '{'}
        
        stack = []
        
        for i in s:
            if i in dic:
                if len(stack) == 0:
                    return False
                top = stack[len(stack) - 1]
                if top == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return len(stack) == 0
                