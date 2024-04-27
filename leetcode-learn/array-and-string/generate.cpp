class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        vector<int> first = {1};
        ans.push_back(first);
        if (numRows == 1) return ans;
        
        vector<int> second = {1, 1};
        ans.push_back(second);
        if (numRows == 2) return ans;
        
        
        // start from third row
        int nCol = 3;
        
        for (int row = 2; row < numRows; row++) {
            vector<int> layer = {1};
            for(int col = 1; col < nCol; col++) {
                if (col == nCol - 1) { // last item
                    layer.push_back(1);
                } else {
                    int n = ans[row - 1][col - 1] + ans[row - 1][col];
                    layer.push_back(n);
                }
            }
            ans.push_back(layer);
            nCol++;
        }
        return ans;
    }
};