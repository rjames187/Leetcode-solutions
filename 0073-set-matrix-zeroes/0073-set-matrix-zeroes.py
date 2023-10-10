class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        marked_rows = set()
        marked_cols = set()
        
        # mark rows and columns
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    marked_rows.add(r)
                    marked_cols.add(c)
        
        # mutate matrix
        for r in range(m):
            if r in marked_rows:
                matrix[r] = [0 for _ in range(n)]
            else:
                for c in marked_cols:
                    matrix[r][c] = 0
        