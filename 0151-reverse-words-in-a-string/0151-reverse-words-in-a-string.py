class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        res = ""
        for char in s:
            if char != " ":
                word += char
            elif word != "":
                res = word + " " + res
                word = ""
        if word != "":
            res = word + " " + res
        return res.strip()