TrieNode = lambda: defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        node = self.root
        for c in word:
            node = node[c]
        node[None] = True

    def search_word(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return None in node

    def startswith(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return True
    
    def get_root(self):
        return self.root


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add_word(w)
        found_words = set()

        def dfs(cy, cx, path, node, visited):
            if (cy, cx) in visited:
                return
            visited.add((cy, cx))
            if None in node:
                found_words.add(path)
            c = board[cy][cx]

            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny, nx = cy+dy, cx+dx
                if 0 <= ny < height and 0 <= nx < width:
                    nc = board[ny][nx]
                    if nc in node:
                        dfs(ny, nx, path+nc, node[nc], visited)
            visited.remove((cy, cx))
            

        height, width = len(board), len(board[0])
        node = trie.get_root()
        for y in range(height):
            for x in range(width):
                c = board[y][x]
                if c in node:
                    dfs(y, x, c, node[c], set())
        
        return list(found_words)
