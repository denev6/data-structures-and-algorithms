class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int len = nums.size();
        
        // heapify by sorting sub trees
        for (int node = len / 2 - 1; node >= 0; node--) {
            heapify(nums, node, len);
        }
        
        // heap-sort
        for (int last = len - 1; last > 0; last--) {
            swap(nums[0], nums[last]);
            heapify(nums, 0, last);
        }
        return nums;
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