class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> ans(rowIndex + 1, 1);
        if (rowIndex == 0 || rowIndex == 1) return ans;
        
        for (int row = 2; row <= rowIndex; row++) {
            int prev_i = ans[0];
            for (int i = 1; i < row; i++) {
                int tmp = ans[i];
                ans[i] = ans[i] + prev_i;
                prev_i = tmp;
            }
        }
        return ans;
    }
};