class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp-style rolling values: best/worst product of a subarray ending at current index
        max_end = min_end = best = nums[0]

        for x in nums[1:]:
            prev_max, prev_min = max_end, min_end

            # three ways to form a subarray ending here:
            # 1) start fresh at x
            # 2) extend previous max
            # 3) extend previous min (important when x is negative)
            max_end = max(x, x * prev_max, x * prev_min)
            min_end = min(x, x * prev_max, x * prev_min)

            best = max(best, max_end)

        return best