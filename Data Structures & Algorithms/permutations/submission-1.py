from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        queue = deque()
        queue.append(([], set()))
        while queue:
            c_l, c_s = queue.popleft()
            if len(c_l) == len(nums):
                perms.append(c_l)
                continue
            
            for n in nums:
                if n not in c_s:
                    queue.append((c_l + [n], c_s | {n}))
        return perms

        