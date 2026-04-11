from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        queue = deque()
        queue.append(set())

        while queue:
            c = queue.popleft()
            print(c)
            if c in res:
                continue
            res.add(frozenset(c))

            for nbr in nums:
                if nbr in c:
                    continue
                queue.append(c|{nbr})        

        return [list(c) for c in res]

        