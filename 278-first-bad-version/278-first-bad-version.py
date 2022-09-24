# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        
        left = 1
        right = n
        while left <= right:
            mid = (right - left) // 2 + left
            
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif not(isBadVersion(mid)) and isBadVersion(mid + 1):
                return mid + 1
            elif isBadVersion(mid):
                right = mid
            elif not isBadVersion(mid):
                left = mid
        
        return mid
            
            