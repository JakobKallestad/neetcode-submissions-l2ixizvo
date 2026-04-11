from typing import List

class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["#"] = True  # end-of-word marker


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add(w)

        height = len(board)
        width = len(board[0]) if height else 0
        res = set()

        def dfs(y: int, x: int, node: dict, path: str, visited: set):
            # If current node ends a word, record it
            if node.get("#"):
                res.add(path)

            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < height and 0 <= nx < width):
                    continue
                if (ny, nx) in visited:
                    continue

                ch = board[ny][nx]
                next_node = node.get(ch)   # safe: returns None if missing
                if not next_node:
                    continue

                visited.add((ny, nx))
                dfs(ny, nx, next_node, path + ch, visited)
                visited.remove((ny, nx))

        for y in range(height):
            for x in range(width):
                ch = board[y][x]
                start_node = trie.root.get(ch)
                if not start_node:
                    continue
                visited = {(y, x)}
                dfs(y, x, start_node, ch, visited)

        return list(res)
