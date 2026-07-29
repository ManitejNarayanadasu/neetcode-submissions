class Solution:
    def groupAnagrams(self, strs):
        grouped = {}
        for i in strs:
            if ''.join(sorted(i)) in grouped:
                grouped[''.join(sorted(i))].append(i)
            else:
                grouped[''.join(sorted(i))] = [i]
        return list(grouped.values())
