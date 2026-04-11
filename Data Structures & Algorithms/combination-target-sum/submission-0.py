class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cumsum, path):
            if cumsum == target:
                res.append(path.copy())
                return
            elif cumsum > target:
                return
            elif i >= len(nums):
                return

            # case 1 --> continue addding current index
            cumsum += nums[i]
            path.append(nums[i])
            dfs(i, cumsum, path)
            path.pop()
            cumsum -= nums[i]

            # case 2 --> move on to next index
            dfs(i+1, cumsum, path)

        

        dfs(0, 0, [])
        return res