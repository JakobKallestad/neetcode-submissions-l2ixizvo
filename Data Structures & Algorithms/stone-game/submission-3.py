class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        piles = deque(piles)  # fast removal on both ends
        memory = {}  # {(n_left, n_right): remembered_state}

        def dfs(piles, n_left, n_right):
            if not piles:
                return 0
            
            if (n_left, n_right) in memory:
                return memory[(n_left, n_right)]

            # take first
            first_tile = piles.popleft()
            take_first = first_tile - dfs(piles, n_left+1, n_right)
            memory[(n_left+1, n_right)] = take_first
            piles.appendleft(first_tile)

            # take last
            last_file = piles.pop()
            take_last = last_file - dfs(piles, n_left, n_right+1)
            memory[(n_left, n_right+1)] = take_last
            piles.append(last_file)

            remaining = max(take_first, take_last)
            memory[(n_left, n_right)] = remaining
            return remaining
                
        return bool(dfs(piles, 0, 0))