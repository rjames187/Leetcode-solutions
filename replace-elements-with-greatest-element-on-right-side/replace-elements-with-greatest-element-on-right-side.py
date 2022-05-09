class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr) - 1):
            result.append(max(arr[i + 1 : len(arr)]))
        result.append(-1)
        return result
        