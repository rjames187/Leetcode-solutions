from collections import Counter, defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = defaultdict(lambda: 0)
        for size in range(minSize, maxSize + 1):
            for i in range(size - 1, len(s)):
                substr = s[i - size + 1: i + 1]
                if len(set(substr)) <= maxLetters:
                    counts[substr] += 1
        if len(counts) == 0: return 0
        return max(counts.values())
                
        
        
        
            
            
        