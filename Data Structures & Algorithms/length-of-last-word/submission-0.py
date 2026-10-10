class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = []
        for word in s.split():
            lst.append(word)
        return len(lst[-1])

        