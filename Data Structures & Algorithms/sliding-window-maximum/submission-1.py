from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        solution = []
        l, r = 0, 0

        while r < len(nums):
            c = nums[r]
            while queue and nums[queue[-1]] < c:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()
            
            if (r + 1) >= k:
                solution.append(nums[queue[0]])
                l += 1
            r += 1
        return solution




        