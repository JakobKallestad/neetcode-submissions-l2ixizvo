class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_substr = 0
        res = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub_len = j-i
                sub_str = s[i:j]
                i2, j2 = i, j
                j2 -= 1
                while i2 <= j2:
                    if s[i2] != s[j2]:
                        break
                    i2 += 1
                    j2 -= 1
                else:
                    if sub_len > longest_substr:
                        longest_substr = sub_len
                        res = sub_str
        return res


# naive solution is just to get all substrings and check palindrome
# DP solution?
# I will like a backtracking with memo might make more sense.