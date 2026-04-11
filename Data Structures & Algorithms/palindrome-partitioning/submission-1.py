class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                k, l = i, j
                while k <= l:
                    if s[k] != s[l]:
                        break
                    k += 1
                    l -= 1
                else:
                    palindromes.add(s[i:j+1])
        
        res = []
        def dfs(i, j, steps):
            left = s[i:j]
            if j == len(s):
                if left in palindromes:
                    steps.append(left)
                    res.append(steps.copy())
                    steps.pop()
                return
            
            # case 1 - CHOP
            if left in palindromes:
                steps.append(left)
                dfs(j, j+1, steps)
                steps.pop()

            # case 2 - DONT
            dfs(i, j+1, steps)


        dfs(0, 1, [])
        return res 



# should be able to iterate through all substrings and then known in O(1) if its a palindrome or not
#
# I see that the backtracking is coming in with how we chop up the input string.
# There are n-1 gaps in which we can either CHOP or DONT. 
# Lets try to code it up with DFS.
# (we can also prune early if we find a branch that does not chop to palindrome)
# (we can also ignore things we have already chopped as it doesn't matter)