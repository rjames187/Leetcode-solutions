class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for ch in ransomNote:
            if ch in magazine:
                magazine.remove(ch)
            else:
                return False
        return True