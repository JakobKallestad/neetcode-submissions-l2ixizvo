class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res1 = sum(range(len(nums)+1))
        res2 = sum(nums)
        return res1-res2