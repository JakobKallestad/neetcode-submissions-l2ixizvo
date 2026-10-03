TrieNode = lambda: defaultdict(TrieNode)

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            node = node[c]
        node[None] = True

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(node, i):
            if i == len(word):
                return None in node
            c = word[i]
            if c == ".":
                for nbr in node:
                    if nbr is not None and dfs(node[nbr], i+1):
                        return True
                return False
            else:
                if c not in node:
                    return False
                return dfs(node[c], i+1)
        
        return dfs(self.root, 0)
