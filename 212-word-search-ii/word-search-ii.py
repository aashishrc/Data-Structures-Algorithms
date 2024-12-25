class Node:

    def __init__(self):
        self.children = {}
        self.is_end_word = False

    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.is_end_word = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()

        for w in words:
            root.addWord(w)
        
        n = len(board)
        m = len(board[0])
        visited = set()
        ans = set()

        def dfs(r, c, node, word):
            if (r < 0 or c <0 or r >= n or c >= m or board[r][c] not in node.children or (r,c) in visited):
                return 

            visited.add((r,c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_end_word:
                ans.add(word)

            res = (dfs(r + 1, c, node, word) or dfs(r-1, c, node, word) or dfs(r, c+ 1, node, word) or dfs(r, c- 1, node, word))

            visited.remove((r,c))
        
        for i in range(n):
            for j in range(m):
                dfs(i, j, root, "")
        return list(ans)