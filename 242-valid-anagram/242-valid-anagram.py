class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        dicts = dict(enumerate(list(s)))
        t = sorted(t)
        dictt = dict(enumerate(list(t)))   
        return dictt == dicts