TrieNode = lambda: defaultdict(TrieNode)

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node[c]
        node[None] = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return None in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True
        
        