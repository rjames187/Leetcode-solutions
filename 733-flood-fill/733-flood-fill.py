class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        start_color = image[sr][sc]
        
        def fill (r, c):
            image[r][c] = color
            
            # up
            if c != len(image[0]) - 1 and image[r][c + 1] == start_color:
                fill (r, c + 1)
            
            # down
            if c != 0 and image[r][c - 1] == start_color:
                fill (r, c - 1)
            
            # right
            if r != len(image) - 1 and image[r + 1][c] == start_color:
                fill (r + 1, c)
            
            # left
            if r != 0 and image[r - 1][c] == start_color:
                fill (r - 1, c)
        
        fill(sr, sc)
        
        return image
                
            