# run time beats 88% of submissions
# memory usage beats 82% of submissions

class Solution:
    def helper(self, digits: str, i: int):
        dic = {"1": ("","",""), "2": ("a","b","c"), "3": ("d", "e", "f"), "4":("g","h","i"), "5": ("j", "k", "l"), "6":("m","n","o"), "7":("p","q","r","s"), "8":("t","u","v"), "9":("w","x","y","z")}
        if i == len(digits):
            if digits == "":
                return []
            return [digits]
        else:
            j = digits[i]
            a = dic[j][0]
            b = dic[j][1]
            c = dic[j][2]
            end = (digits[i + 1:] if i < len(digits) else "")
            expa = self.helper(digits[:i] + a + end, i + 1)
            expb = self.helper(digits[:i] + b + end, i + 1)
            expc = self.helper(digits[:i] + c + end, i + 1)
            if len(dic[j]) == 4:
                d = dic[j][3]
                expd = self.helper(digits[:i] + d + end, i + 1)
                return expa + expb + expc + expd
            else:
                return expa + expb + expc
    
    def letterCombinations(self, digits: str) -> List[str]:
        return self.helper(digits, 0)
    
    
        
