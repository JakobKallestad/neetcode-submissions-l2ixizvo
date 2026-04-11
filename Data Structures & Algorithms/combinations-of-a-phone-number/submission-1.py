class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2': list("abc"),
            '3': list("def"),
            '4': list("ghi"),
            '5': list("jkl"),
            '6': list("mno"),
            '7': list("pqrs"),
            '8': list("tuv"),
            '9': list("wxyz"),
        }

        res = []
        def dfs(i, current):
            if i == len(digits):
                res.append(''.join(current))
                return
            
            for c in digit_map[digits[i]]:
                current.append(c)
                dfs(i+1, current)
                current.pop()

        dfs(0, [])
        return [] if res[0] == "" else res


# could do a BFS. Would be fast, but use a lot of memory.
# could do a normal DFS. but try to not use memory. is that backtracking?