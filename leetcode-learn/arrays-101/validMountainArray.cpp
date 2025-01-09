// Valid Mountain Array

class Solution {
public:
    bool validMountainArray(vector<int>& arr) { 
        int prev = arr[0];
        int i, current;

        // 상승
        for (i = 1; i < arr.size(); i++) {
            current = arr[i];
            if (prev == current) return false;
            if (prev > current) {
                if (i == 1) return false;
                break;
            };
            prev = current;
        }
        if (i == arr.size()) return false; // 올라가기만 하면 안 됨
        
        // 하강
        for (; i < arr.size(); i++) {
            current = arr[i];
            if (prev <= current) return false;
            prev = current;
        }
        return true;
    }
};