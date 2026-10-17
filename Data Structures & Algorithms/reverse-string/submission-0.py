class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        rev = []
        for i in range(len(s)-1,-1,-1):
            rev.append(s[i])
        for i in range(len(s)):
            s[i] = rev[i]
        