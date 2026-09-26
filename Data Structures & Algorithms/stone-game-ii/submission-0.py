from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        suffix = [0] * (len(piles) + 1)

        for i in range(len(piles) - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        @cache
        def dfs(l, m):
            if l >= len(piles):
                return 0

            # take first
            best = 0
            max_x = min(2 * m, len(piles) - l)
            for x in range(1, max_x + 1):
                opponent = dfs(l + x, max(m, x))
                mine = suffix[l] - opponent

                best = max(best, mine)

            return best
                
        return dfs(0, 1)