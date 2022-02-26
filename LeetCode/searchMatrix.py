# runtime beats 64% of python3 submissions
# using binary search rather than basic linear search greatly reduces run time
# binary search complexity is O(log n) while linear search complexity is O(n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        low = 0
        high = len(matrix) - 1

        while low <= high:
               
            mid = low + (high - low) // 2
            
            first_elem = matrix[mid][0]
            last_elem = matrix[mid][len(matrix[mid]) - 1]
            
            # Found our element, return.
            if target >= first_elem and target <= last_elem:
                row = matrix[mid]
                break

            # Construct search space since we know
            # the list is sorted.
            if last_elem < target:
                low = mid + 1
            else:
                
                high = mid - 1
            #print(low, mid, high)
            
        if row == -1:
            return False  
        # second binary search
        low = 0
        high = len(row) - 1

        while low <= high:

            mid = low + (high - low) // 2

            # Found our element, return.
            if row[mid] == target:
                return True

            # Construct search space since we know
            # the list is sorted.
            if row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
