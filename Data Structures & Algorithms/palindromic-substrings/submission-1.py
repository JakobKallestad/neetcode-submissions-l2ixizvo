class Solution:
    def countSubstrings(self, s: str) -> int:
        n_palindromes = 0

        for i in range(len(s)):
            
            # odd
            l, r = i, i
            while 0 <= l <= r < len(s):
                if s[l] == s[r]:
                    n_palindromes += 1
                else:
                    break
                l -= 1
                r += 1

            # even
            l, r = i, i+1
            while 0 <= l <= r < len(s):
                if s[l] == s[r]:
                    n_palindromes += 1
                else:
                    break
                l -= 1
                r += 1
        
        return n_palindromes