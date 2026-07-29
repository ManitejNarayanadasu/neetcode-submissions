class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}

        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        sorted_dict = dict(sorted(result.items(), key=lambda item: item[1]))
            
        return list(sorted_dict.keys())[-k:]
        