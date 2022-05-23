class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        hash_table_s = {}
        for i in s:
            if i in hash_table_s:
                hash_table_s[i] += 1
            else:
                hash_table_s[i] = 1
        
        hash_table_t = {}
        for i in t:
            if i in hash_table_t:
                hash_table_t[i] += 1
            else:
                hash_table_t[i] = 1
        
        return hash_table_s == hash_table_t
               