from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c_nums = Counter(nums)
        return c_nums.most_common(1)[0][0]