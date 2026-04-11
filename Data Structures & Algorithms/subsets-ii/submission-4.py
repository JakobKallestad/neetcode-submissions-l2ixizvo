from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] #set()
        candidates = list(Counter(nums).items())
        print(candidates)

        def dfs(i, j, cumsum, path):
            if i == len(candidates):
                res.append(path.copy())
                return
            #res.add(tuple(sorted(path.copy())))
            
            if j < candidates[i][1]:
                # case 1 --> continue addding current index
                path.append(candidates[i][0])
                dfs(i, j+1, cumsum+candidates[i][0], path)
                path.pop()

            # case 2 --> move on to next index
            dfs(i+1, 0, cumsum, path)

        

        dfs(0, 0, 0, [])  # i, j, cumsum, path
        return [list(r) for r in res]



        