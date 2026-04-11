class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        res = set()
        n2 = n*2

        def dfs(cur, o_p, c_p):
            if len(cur) == n2:
                #res.append(cur)
                res.add(cur)
                return
            
            # A) add open
            if o_p < n:
                n_cur = cur + "("
                dfs(n_cur, o_p+1, c_p)

            # B) add closed
            if c_p < o_p:
                n_cur = cur + ")"
                dfs(n_cur, o_p, c_p+1)           

        dfs("", 0, 0)
        #return res
        return [r for r in res]

# current thinking:
# I think I can explore all solutions by always putting the next ()-pair either:
# A) in front
# B) after
# C) outside
# I'm not sure why I think that this is the case yet.