from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @cache
        def dfs(l, r):
            if l == r:
                return 0

            # take first
            take_first = piles[l] - dfs(l+1, r)

            # take last
            take_last = piles[r] - dfs(l, r-1)

            return max(take_first, take_last)
                
        return dfs(0, len(piles)-1) > 0