class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        need = {}
        window = {}
        have = 0
        need_count = 0
        min_length = float("inf")
        start = 0
        for i in t:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1
        for right in range(len(s)):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            need_count = len(need.keys())
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            while need_count == have:
                length = right - left + 1
                if length < min_length:
                    min_length = length
                    start = left
                if s[left] in need:
                    window[s[left]] -= 1
                    if window[s[left]] < need[s[left]]:
                        have -= 1
                left += 1
        if min_length == float("inf"):
            return ""
        return s[start:start + min_length]
            

        