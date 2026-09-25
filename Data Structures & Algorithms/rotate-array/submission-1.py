class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_shifted = [None]*len(nums)

        for i in range(len(nums)):
            target_index = (i+k)%len(nums)
            target = nums[target_index]
            nums_shifted[target_index] = nums[i]
        
        for i in range(len(nums)):
            nums[i] = nums_shifted[i]
        