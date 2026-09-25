class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #piles = deque(piles)  # fast removal on both ends
        memory = {}  # {(n_left, n_right): remembered_state}

        def dfs(l, r, n_left, n_right):
            if l == r:
                return 0
            
            if (n_left, n_right) in memory:
                return memory[(n_left, n_right)]

            # take first
            first_tile = piles[l]
            take_first = first_tile - dfs(l+1, r, n_left+1, n_right)

            # take last
            last_file = piles[r]
            take_last = last_file - dfs(l, r-1, n_left, n_right+1)

            remaining = max(take_first, take_last)
            memory[(n_left, n_right)] = remaining
            return remaining
                
        return bool(dfs(0, len(piles)-1, 0, 0))