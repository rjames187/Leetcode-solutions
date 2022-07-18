class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while (True):
            summ = numbers[i] + numbers[j]
            if summ > target:
                j -= 1
            elif summ < target:
                i += 1
            else:
                return [i + 1, j + 1]