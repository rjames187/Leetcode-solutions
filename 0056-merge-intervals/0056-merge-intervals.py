class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        cur_int = intervals[0]
        for interv in intervals:
            if interv[0] <= cur_int[1]:
                cur_int[1] = max(cur_int[1], interv[1])
            else:
                res.append(cur_int)
                cur_int = interv
        res.append(cur_int)
        return res