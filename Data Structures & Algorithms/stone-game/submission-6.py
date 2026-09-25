from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @cache
        def dfs(l, r, n_left, n_right):
            if l == r:
                return 0

            # take first
            first_tile = piles[l]
            take_first = first_tile - dfs(l+1, r, n_left+1, n_right)

            # take last
            last_file = piles[r]
            take_last = last_file - dfs(l, r-1, n_left, n_right+1)

            remaining = max(take_first, take_last)
            return remaining
                
        return bool(dfs(0, len(piles)-1, 0, 0))