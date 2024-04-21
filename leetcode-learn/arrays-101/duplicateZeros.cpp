// Duplicate Zeros

class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        vector<int> ans(arr.size());
        int pointer = 0;
        for (int i = 0; i < arr.size(); i++) {
            int n = arr[i];
            ans[pointer] = n;
            pointer++;
            if (n == 0 && pointer < ans.size()) {
                ans[pointer] = 0;
                pointer++;
            }
            if (pointer == arr.size()) break;
        }
        arr = ans;
    }
};