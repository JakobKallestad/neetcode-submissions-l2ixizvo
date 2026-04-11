from collections import defaultdict
import string

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # ensure correct input:
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                w1, w2 = words[i], words[j]
                if len(w2) < len(w1) and w1.startswith(w2):
                    return ""
        
        graph = defaultdict(set)  # before_rules --> before(a, b) --> before[b].append(a) --> in order to do b, we must first do "a" and the other requirements first.
        all_prefixes = set()
        all_characters = set()
        for word in words:  # N
            for i in range(len(word)):  # N
                all_characters.add(word[i])
                prefix = word[:i]
                temp_rules = []
                if prefix not in all_prefixes:
                    all_prefixes.add(prefix)
                    for w2 in words:  # N
                        if w2.startswith(prefix) and len(w2) > i:
                            temp_rules.append(w2[i])
                #temp_rules = list(dict.fromkeys(temp_rules))  # remove duplicates
                if len(temp_rules) >= 2:
                    add_set = set()
                    for c in temp_rules[::-1]:
                        graph[c].update(add_set)
                        add_set.add(c)
        for k, v in graph.items():
            graph[k].discard(k)
        print(graph)

        # successfully buildt the graph from all prefixes, hopefully it doesnt kill the runtime.

        visiting = set()   # nodes in current DFS stack
        visited = set()    # nodes fully processed
        order = []         # postorder; reverse at end

        def dfs(u: str) -> bool:
            if u in visiting:     # cycle
                return False
            if u in visited:      # already done
                return True

            visiting.add(u)
            for v in graph[u]:
                if not dfs(v):
                    return False
            visiting.remove(u)

            visited.add(u)
            order.append(u)
            return True

        for c in all_characters:
            if not dfs(c):
                return ""

        return ''.join(order[::-1])





# cool task:
# I know its a graph task, but otherwise im a bit lost initially
# .
# I guess we know that the first character of the last word is at least
# smaller then all the other words' first characters
# .
# h -> e -> r
# (r -> n)
# (n -> f)
# .
# First example is easy, but not sure if that will stick
# .
# basically for all the words that have the SAME prefix then we can potentially learn an ordering based on
# the next character in those words
# This is also why it works for the first character in all the words because they all share the same PREFIX
# which in that case is "".
# .
# So one way to think about this is to figure out ALL PREFIXES that we can make and then based on that figure
# out which words have prefix P1 and from there write down before_rules in the form before(a, b) which means
# that a comes before b
# .
# After we have all these rules we can start with ALL the characters that have NO before_rules.
# We can add all of these characters to the solution in any order. (BFS?)
# we might be able to continously add more and more characters after that point.
# .
# A challenge will be to find all the before_rules though, because it means we need to find ALL the PREFIXES.
# Could a TRIE help with this?
# I think I could kind of just brute force this part though.
# its only maximum 100 prefixes per word and then 100 words. And for each prefix I need to see if it is new,
# If that is the case then I need to look at all the words and see which word has this prefix.
# So if N = 100, then its prefixes=N^2, and time to check word_i --> using str.startswith(). worst case N.
# So N^3
# Its fine...

