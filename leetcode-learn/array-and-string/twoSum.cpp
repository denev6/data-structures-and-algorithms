class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int startPointer = 0;
        int endPointer = numbers.size() - 1;
        while (startPointer < endPointer) {
            int sum = numbers[startPointer] + numbers[endPointer];
            if (sum == target) break;
            else if (sum > target) endPointer--;
            else startPointer++;
        }
        vector<int> ans = {++startPointer, ++endPointer};
        return ans;
    }
};