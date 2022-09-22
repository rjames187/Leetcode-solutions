class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(t)) == sorted(list(s))