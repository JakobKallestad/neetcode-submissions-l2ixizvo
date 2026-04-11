from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = list(Counter(candidates).items())
        print(candidates)

        def dfs(i, j, cumsum, path):
            if cumsum == target:
                res.append(path.copy())
                return
            elif cumsum > target:
                return
            elif i == len(candidates):
                return
            
            if j < candidates[i][1]:
                # case 1 --> continue addding current index
                path.append(candidates[i][0])
                dfs(i, j+1, cumsum+candidates[i][0], path)
                path.pop()

            # case 2 --> move on to next index
            dfs(i+1, 0, cumsum, path)

        

        dfs(0, 0, 0, [])  # i, j, cumsum, path
        return res