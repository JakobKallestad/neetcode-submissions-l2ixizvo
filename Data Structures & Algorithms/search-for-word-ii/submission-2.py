from collections import defaultdict

class Trie:
    def __init__(self):
        self.root = defaultdict(dict)

    def add(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = defaultdict(dict)
            node = node[ch]
        node["#"] = True   # end-of-word marker

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return "#" in node

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        height = len(board)
        width = len(board[0])

        def dfs(cy, cx, visited, depth, node):
            if depth == 11:
                return
            
            # progress node from prev to current
            c = board[cy][cx]
            if c not in node:
                node[c] = defaultdict(dict)
            node = node[c]
            
            # explore valid and unexplored next positions
            for (dy, dx) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
                ny = cy + dy
                nx = cx + dx
                if (ny, nx) not in visited and (0 <= ny < height and 0 <= nx < width):
                    visited.add((ny, nx))  # add
                    dfs(ny, nx, visited, depth+1, node)
                    visited.remove((ny, nx))  # undo
                

        for y in range(height):
            for x in range(width):
                visited = {(y, x)}
                dfs(y, x, visited, 0, trie.root)

        
        res = []
        for word in words:
            if trie.starts_with(word):
                res.append(word)
        return res




# Thinking:
# I will obviously need a trie
# The board is somewhat small. Max size 12. Also word max size 10 is VERY helpful
# .
# I will go through each (y, x) coordinate in the board and run a DFS + Trie + Backtracing to construct the Trie
# The root of the Trie will have children to each of the squares on the board
# Then I will go over each word to see if they are in the Trie (board).
# .
# This is important because storing the Trie should be significantly less SPACE then storing all possible word combinations.
#