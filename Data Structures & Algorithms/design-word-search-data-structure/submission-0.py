class TrieNode:
    def __init__(self):
        self.children = {} # str --> TrieNode
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        

    def search(self, word: str) -> bool:
        root = self.root

        candidates = [root]
        for c in word:
            if not candidates:
                return False
            new_candidates = []
            if c == ".":
                for node in candidates:
                    for ch in node.children:
                        new_candidates.append(node.children[ch])
            else:
                for node in candidates:
                    if c in node.children:
                        new_candidates.append(node.children[c])
            candidates = new_candidates
        for c in candidates:
            if c.is_word:
                return True
        return False


# THinking:
# I think that while searching i just need to maintain a listof candidates
