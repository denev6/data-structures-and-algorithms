class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> original = heights; // deep copy
        bubbleSort(heights);
        int cnt = 0;
        for (int i = 0; i < heights.size(); i++) {
            if (heights[i] != original[i]) cnt++;
        }
        return cnt;
    }
    
    void bubbleSort(vector<int>& arr) {
        bool isSwaped = true;
        while (isSwaped) {
            isSwaped = false;
            for (int i = 0; i < arr.size() - 1; i++) {
                if (arr[i] > arr[i + 1]) {
                    swap(arr[i], arr[i + 1]);
                    isSwaped = true;
                }
            }
        }
    }
};