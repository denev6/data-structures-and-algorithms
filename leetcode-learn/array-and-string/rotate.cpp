// Could you do it in-place with O(1) extra space?

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k % nums.size(); // if not, overflow when k > nums.size().
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin() + k);
        reverse(nums.begin() + k, nums.end());
    }
};