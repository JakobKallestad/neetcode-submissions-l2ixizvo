class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = [False]*len(nums)
        ans[-1] = True
        c_pos = 0
        for i in range(len(nums)-2, -1, -1):
            c = nums[i]
            for j in range(min(c+1, len(nums)-i)):
                if ans[i+j]:
                    ans[i] = True
        return ans[0]
