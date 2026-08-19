class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last != match[char]:
                    return False
        return not stack