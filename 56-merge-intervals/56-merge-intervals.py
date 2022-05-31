class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        solution = []
        
        def first_tup_item (tup):
            return tup[0]
        
        intervals = sorted(intervals, key=first_tup_item)
        
        stage = intervals[0]
        
        for i in range (1, len(intervals)):
            if intervals[i][0] > stage[1]:
                solution.append(stage)
                stage = intervals[i]
            elif intervals[i][1] > stage[1]:
                stage = [stage[0], intervals[i][1]]
        solution.append(stage)
        
        return solution
        