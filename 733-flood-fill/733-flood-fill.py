from copy import deepcopy
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        def fill (sr, sc, old_color, new_color):
            if sr < 0 or sc < 0 or sr == len(image) or sc == len(image[0]) or image[sr][sc] != old_color:
                return
            image[sr][sc] = new_color
            fill(sr + 1, sc, old_color, new_color)
            fill(sr - 1, sc, old_color, new_color)
            fill(sr, sc + 1, old_color, new_color)
            fill(sr, sc - 1, old_color, new_color)
        
        fill(sr, sc, image[sr][sc], color)
        
        return image
            