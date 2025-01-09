class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int len = nums.size();
        // target index when "nums" is sorted in ascending order
        int target = len - k;
        
        // heap-sort until finding the target
        for (int node = len / 2 - 1; node >= 0; node--) {
            heapify(nums, node, len);
        }
        for (int last = len - 1; last >= target; last--) {
            swap(nums[0], nums[last]);
            heapify(nums, 0, last);
        }
        return nums[target];
    }
    void heapify(vector<int>& arr, int root, int last) {
        int largest = root;
        int left = root * 2 + 1;
        int right = root * 2 + 2;
        
        if (left < last && arr[left] > arr[largest]) largest = left;
        if (right < last && arr[right] > arr[largest]) largest = right;
        if (largest != root) {
            swap(arr[largest], arr[root]);
            heapify(arr, largest, last);
        }
    }
};