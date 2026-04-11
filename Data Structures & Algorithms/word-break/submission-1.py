from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False]*len(s)

        def make_trie():
            return defaultdict(make_trie)
        
        trie = make_trie()

        for word in wordDict:
            node = trie
            for c in word:
                node = node[c]
            node["#"] = True

        for i in range(len(dp)):
            if dp[i]: # update future DP instances indicating where we can go from here
                c_word = s[i:]
                #for w in wordDict:
                #    if c_word.startswith(w):
                #        dp[i+len(w)] = True

                node = trie
                for j, c in enumerate(c_word, start=1):
                    if c not in node:
                        break
                    node = node[c]
                    if "#" in node:
                        dp[i+j] = True
        print(dp)
        return dp[-1]



# Thinking:
# I should be able to take the starting word and break check for all words in my wordlist if my word starts
# with each word in the wordlist.
# For those words that this was the case i know we can get to a certain index in the word by using this.
# because they are not asking for paths or number of words used or duplications or anything this is simple.
# Just update the DP array with places i was able to go to
# .
# Possible improvement --> Create a TRIE out of the words in the wordDict. I think would allow me to even faster
# determine how far we can go.
# Actually lets just do that. Seems easy enough.
# .
# Meh, ill do naive first.