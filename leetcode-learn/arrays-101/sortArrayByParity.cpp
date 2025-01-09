// Sort Array By Parity

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int evenPointer = 0;
        for (int i = 0; i < nums.size(); i++) {
            int current = nums[i];
            if (current % 2 == 0) {
                nums[i] = nums[evenPointer];
                nums[evenPointer] = current;
                evenPointer++;
            }
        }
        return nums;
    }
};