import string

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) < 2:
            return 1

        c_map = {str(k): v for k, v in zip(range(1, 27), string.ascii_uppercase)}  # 1..26
        dp = [1, 1] + [0] * len(s)  # dp[0]=1 empty prefix, dp[1]=1 since s[0] != '0'

        for i in range(2, len(s) + 2):
            s2 = s[i - 2]           # one digit
            d1 = s[i - 3:i - 1]     # two digits
            res1 = dp[i - 1] if s2 in c_map else 0
            res2 = dp[i - 2] if d1 in c_map else 0
            dp[i] = res1 + res2

        return dp[-1]