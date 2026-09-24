class Solution:
    def jump(self, nums: List[int]) -> int:
        current_steps = 0
        step_start = 0
        step_end = 0
        while step_end < len(nums)-1:
            next_step_start = step_end+1
            next_step_end = step_end+1

            for i in range(step_start, step_end+1):
                e = nums[i]
                next_step_end = max(next_step_end, i+e)
            
            step_start = next_step_start
            step_end = next_step_end
            current_steps += 1
        return current_steps
            





