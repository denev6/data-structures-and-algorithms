// Replace Elements with Greatest Element on Right Side

class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int largest = arr[arr.size()-1];
        arr[arr.size()-1] = -1;
        for (int i = arr.size() - 2; i >= 0; i--) {
            int current = arr[i];
            arr[i] = largest;
            if (current > largest) {
                largest = current;
            }
        }
        return arr;
    }
};