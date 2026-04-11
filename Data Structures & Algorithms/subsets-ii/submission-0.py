from itertools import combinations

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = set()
        for r in range(len(nums) + 1):
            for c in combinations(nums, r):
                out.add(c)          # tuples are hashable
        return [list(t) for t in sorted(out)]