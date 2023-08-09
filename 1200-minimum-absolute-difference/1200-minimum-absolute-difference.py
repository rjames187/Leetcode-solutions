class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        min_diff = float('inf')
        arr.sort()
        for i in range(1, len(arr)):
            a = arr[i - 1]
            b = arr[i]
            diff = abs(b - a)
            if diff < min_diff:
                min_diff = diff
                res = [[a, b]]
            elif diff == min_diff:
                res.append([a, b])
        return res
        