// Merge Sorted Array
// Follow up: Can you come up with an algorithm that runs in O(m + n) time?

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int pointer1 = m - 1, pointer2 = n - 1, pointerAll = m + n - 1;
        while (pointer2 >= 0) {
            if (pointer1 >= 0 && nums1[pointer1] > nums2[pointer2]) {
                nums1[pointerAll--] = nums1[pointer1--];
            } else {
                nums1[pointerAll--] = nums2[pointer2--];
            }
        }
    }
};