class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def add(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c]= TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res = set()
        visited = set()
        for word in words:
            root.add(word)
        ROWS,COLS = len(board),len(board[0])
        def dfs(r,c,node,word):
            if r<0 or c< 0 or r>=ROWS or c>=COLS or board[r][c] not in node.children or (r,c) in visited:
                return False
            visited.add((r,c))
            word+=board[r][c]
            #update the node
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
            dfs(r+1,c,node,word) 
            dfs(r-1,c,node,word) 
            dfs(r,c+1,node,word) 
            dfs(r,c-1,node,word) 
            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        return list(res)