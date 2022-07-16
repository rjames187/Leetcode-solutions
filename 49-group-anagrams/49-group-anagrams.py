class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strs.sort()
        
        def stringToTuple (str):
            lst = []
            for i in str:
                lst.append(i)
            return tuple(sorted(lst))
        
        groups = {}
        
        for i in strs:
            key = stringToTuple(i)
            if key in groups:
                groups[key].append(i)
            else:
                groups[key] = [i]
        
        result = []
        
        for i in groups:
            result.append(groups[i])
        
        return result
                
            
            