class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap = defaultdict(list)
        colmap= defaultdict(list)
        gridmap = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j]=="." :
                    continue

                if (board[i][j] in rowmap[i] 
                    or board[i][j] in colmap[j] 
                    or board[i][j] in gridmap[(i // 3, j // 3)]):
                    return False

                rowmap[i].append(board[i][j])
                colmap[j].append(board[i][j])
                gridmap[(i // 3, j // 3)].append(board[i][j])
        return True