class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int first = nums[0], second = -1;
        int firstIdx = 0, secondIdx = -1;
        
        for (int i = 1; i < nums.size(); i++) {
            int val = nums[i];
            if (first < val) {
                second = first;
                secondIdx = firstIdx;
                first = val;
                firstIdx = i;
            } else if (second < val) {
                second = val;
                secondIdx = i;
            }
        }
        
        if (second * 2 <= first) return firstIdx;
        return -1;
    }
};