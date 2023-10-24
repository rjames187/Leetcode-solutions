class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if c in pairs:
                if len(stack) == 0:
                    return False
                if stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
            
        