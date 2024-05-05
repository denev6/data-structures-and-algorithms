class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        vector<vector<int>> ans;
        
        int minDiff = INT_MAX;
        for(int i = 1; i < arr.size(); i++) {
            int diff = arr[i] - arr[i - 1];
            if (minDiff > diff) {
                minDiff = diff;
                ans.clear();
                ans.push_back({arr[i - 1], arr[i]});
            } else if (minDiff == diff) {
                ans.push_back({arr[i - 1], arr[i]});
            }
        }
        return ans;
    }
};