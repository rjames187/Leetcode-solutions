class Solution:
    def getAverage(self, coords: List[int], img: list[List[int]]):
        DELTA = [-1, 0, 1]
        row, col = coords
        total = 0
        count = 0
        for rd in DELTA:
            nr = row + rd
            if nr >= len(img) or nr < 0:
                continue
            for cd in DELTA:
                nc = col + cd
                if nc >= len(img[0]) or nc < 0:
                    continue
                total += img[nr][nc]
                count += 1
        return floor(total / count)
                
                
        
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [[None for i in range(len(img[0]))] for i in range(len(img))]
        for r in range(len(img)):
            for c in range(len(img[r])):
                average = self.getAverage([r, c], img)
                res[r][c] = average
        return res
        