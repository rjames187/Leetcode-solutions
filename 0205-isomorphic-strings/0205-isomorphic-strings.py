class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_used = set()
        for i in range(len(s)):
            s_chr = s[i]
            t_chr = t[i]
            
            if s_chr in s_map:
                if s_map[s_chr] != t_chr:
                    return False
            else:
                if t_chr in t_used:
                    return False
                s_map[s_chr] = t_chr
                t_used.add(t_chr)
                
                
        return True