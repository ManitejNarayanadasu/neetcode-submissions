class Solution:
    def groupAnagrams(self, strs):
        grouped = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in grouped:
                grouped[key].append(i)
            else:
                grouped[key] = [i]
        return list(grouped.values())
