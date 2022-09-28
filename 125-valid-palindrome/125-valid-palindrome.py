class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(lambda ch: ch.isalnum(), s))
        s = ''.join(s)
        s = s.lower()
        return s == s[::-1]