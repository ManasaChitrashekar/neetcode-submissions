class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> sudoku = new HashSet<>();
        for(int i =0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                if('.'!=board[i][j])
                {
                    if(!sudoku.add("row"+i+board[i][j]))
                        return false;
                    if(!sudoku.add("col"+j+board[i][j]))
                        return false;
                    //I struggled to calculate this case
                    if(!sudoku.add("box"+(i/3)+(j/3)+board[i][j]))
                        return false;
                }
            }
        }
        return true;
    }
}
