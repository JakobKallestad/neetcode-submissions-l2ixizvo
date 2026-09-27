class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                # minimum must be to the right of m
                l = m + 1
            else:
                # m could itself be the minimum
                r = m

        return nums[l]