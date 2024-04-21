// Move Zeroes

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int pointer = 0;
        for (int i = 0; i < nums.size(); i++) {
            int current = nums[i];
            if (current != 0) {
                nums[pointer] = current;
                pointer++;
            }
        }
        for (int i = pointer; i < nums.size(); i++) {
            nums[i] = 0;
        }
    }
};