class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wrd1 = {}
        wrd2 = {}
        for char in s:
            if char in wrd1:
                wrd1[char] += 1
            else:
                wrd1[char] = 1
        for char in t:
            if char in wrd2:
                wrd2[char] += 1
            else:
                wrd2[char] = 1
        if wrd1 == wrd2:
            return True
        return False


        