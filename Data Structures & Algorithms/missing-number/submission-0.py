class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums)
        for i in range(num):
            num ^= i ^ nums[i]
        return num
        