from collections import deque

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        perms = set()
        queue = deque()
        c_nums = dict(Counter(nums))
        queue.append(([], c_nums))
        while queue:
            c_l, c_s = queue.popleft()
            #print(c_l)
            
            #if len(c_l) == len(nums):
            perms.add(tuple(sorted(c_l)))
            
            for n in nums:
                if c_s[n] > 0:
                    n_s = c_s.copy()
                    n_s[n] -= 1
                    queue.append((c_l + [n], n_s))
        return [list(p) for p in perms]