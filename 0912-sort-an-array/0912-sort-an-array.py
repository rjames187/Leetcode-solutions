class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_arr, right_arr):
            l, r = 0, 0
            res = []
            while True:
                if l >= len(left_arr) and r >= len(right_arr):
                    break
                elif l >= len(left_arr):
                    res.append(right_arr[r])
                    r +=1
                elif r >= len(right_arr):
                    res.append(left_arr[l])
                    l += 1
                elif left_arr[l] < right_arr[r]:
                    res.append(left_arr[l])
                    l += 1
                else:
                    res.append(right_arr[r])
                    r += 1
            return res
        def mergeSort(arr):
            if len(arr) > 1:
                m = (0 + len(arr) - 1) // 2
                
                left_arr = mergeSort(arr[:m + 1])
                right_arr = mergeSort(arr[m + 1:])
                arr = merge(left_arr, right_arr)
            return arr
        return mergeSort(nums)
                
        