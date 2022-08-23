class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(filter(lambda i: (i.isalnum()), s))
        print(s)
        # two pointers solution
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True