class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        cur = None
        res = []
        for interval in intervals:
            if cur == None:
                cur = interval
                continue
            x1, x2 = cur
            y1, y2 = interval
            # check for overlap
            if x2 >= y1:
                cur = [x1, max(x2, y2)]
                continue
            # no overlap
            res.append(cur)
            cur = interval
        res.append(cur)
        return res