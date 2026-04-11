class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        reachable = {0}

        for c in nums:
            next_reachable = set()
            for s in reachable:
                if s + c == target:
                    return True
                if s + c < target:
                    next_reachable.add(s + c)
            reachable |= next_reachable

        return target in reachable
