class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            if not newInterval:
                res.append(interval)
                continue
            x1, x2 = interval
            y1, y2 = newInterval
            is_before = x2 < y1
            is_after = y2 < x1
            if not(is_before or is_after):
                newInterval = [min(x1, y1), max(x2, y2)]
            elif is_before:
                res.append(interval)
            elif is_after:
                res.append(newInterval)
                newInterval = None
                res.append(interval)
        if newInterval:
            res.append(newInterval)
            
        return res
            
            