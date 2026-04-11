class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i, chars in enumerate(zip(*strs)):
            c = chars[0]
            if not all(c == c2 for c2 in chars):
                return strs[0][:i]
        min_len = min(len(s) for s in strs)
        return strs[0][:min_len]