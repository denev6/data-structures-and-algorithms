class Solution {
public:
    void sortColors(vector<int>& nums) {
        selectionSort(nums);
    }
    
    void selectionSort(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            int minIdx = i;
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[minIdx] > nums[j]) {
                    minIdx = j;
                }
            }
            swap(nums[i], nums[minIdx]);
        }
    }
};