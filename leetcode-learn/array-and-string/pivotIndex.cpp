class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total = 0;
        for (int n : nums) {
            total += n;
        }
        
        int partial = 0;
        for (int pointer = 0; pointer < nums.size(); pointer++) {
            int val = nums[pointer];
            total -= val;
            if (partial == total) return pointer;
            partial += val;
        }
        return -1;
    }
};