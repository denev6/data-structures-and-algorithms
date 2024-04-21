// Remove Element

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int pointer = 0;
        for (int i = 0; i < nums.size(); i++) {
            int current = nums[i];
            if (current != val) {
                nums[pointer] = current;
                pointer++;
            }
        }
        return pointer;
    }
};