class Solution {
    // Ref: https://walkccc.me/LeetCode/problems/498
    public: vector<int> findDiagonalOrder(vector<vector<int>> &matrix) {
        const int nRow = matrix.size();
        const int nCol = matrix[0].size();
        vector<int> ans(nRow * nCol);
        
        int d = 1; // direction: left-bottom(-), right-top(+)
        int row = 0;
        int col = 0;

        for (int i = 0; i < ans.size(); i++) {
            ans[i] = matrix[row][col];
            row -= d;
            col += d;
            
            // out-of-bounds
            if (row == nRow) // bottom
                row = nRow - 1, col += 2, d = -d;
            if (col == nCol) // right
                col = nCol - 1, row += 2, d = -d;
            if (row < 0) // top
                row = 0, d = -d;
            if (col < 0) // left
                col = 0, d = -d;
        }
        return ans;
    }
};