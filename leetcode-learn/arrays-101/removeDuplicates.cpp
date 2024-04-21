// Remove Duplicates from Sorted Array

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int pointer = 0;
        int previous = 101; // 문제 조건: -100 <= nums[i] <= 100
        for (int i = 0; i < nums.size(); i++) {
            int current = nums[i];
            if (current != previous) {
                nums[pointer] = current;
                previous = current;
                pointer++;
            }
        }
        return pointer;
    }
};