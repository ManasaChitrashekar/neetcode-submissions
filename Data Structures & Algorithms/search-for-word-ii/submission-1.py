class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False

    def add(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c]= TrieNode()
            cur = cur.children[c]
        cur.endofWord= True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add(word)
        ROWS,COLS = len(board),len(board[0])
        res,visited = set(),set()
        def dfs(i,j,node,word):
            if i<0 or i == ROWS or j<0 or j==COLS or (i,j) in visited or board[i][j] not in node.children:
                return 
            visited.add((i,j))
            word +=board[i][j]
            node = node.children[board[i][j]]
            if node.endofWord:
                res.add(word)
            
            dfs(i+1,j,node,word)
            dfs(i-1,j,node,word)
            dfs(i,j+1,node,word)
            dfs(i,j-1,node,word)

            visited .remove((i,j))
            return 

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        return list(res)