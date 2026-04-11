from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)
        wordList.append(beginWord)

        def check_levenshtein1(w1, w2):
            w1, w2 = wordList[i], wordList[j]
            if len(w1) != len(w2):
                return False
            n_different = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    n_different += 1
                    if n_different == 2:
                        return False
            return True

        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                w1, w2 = wordList[i], wordList[j]
                if check_levenshtein1(w1, w2):
                    graph[w1].append(w2)
                    graph[w2].append(w1)
        
        
        print(graph)
        
        visited = set()
        queue = deque([(beginWord, 1)])
        while queue:
            c_word, c_depth = queue.popleft()
            if c_word in visited:
                continue
            if c_word == endWord:
                return c_depth
            visited.add(c_word)

            for n_word in graph[c_word]:
                queue.append((n_word, c_depth+1))
        return 0

# What we know:
# There are not really that many words. So we can check for each word the ones that it can go to next.
# The words are not that long. So its basically constant time to check any pair for one different character.
# Then comes the actual difficult part?
# We could just BFS traverse this
# Isn't that just it?