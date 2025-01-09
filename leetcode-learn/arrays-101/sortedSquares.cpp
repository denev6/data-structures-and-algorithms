// Squares of a Sorted Array
/* Follow up: Squaring each element and sorting the new array is very trivial, 
    could you find an O(n) solution using a different approach? */ 

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> ans(nums.size(), 0);
        int ansPointer = ans.size() - 1;
        
        int endPointer = nums.size() - 1;
        int startPointer = 0;
        
        while(startPointer <= endPointer) {
            int startSquared = nums[startPointer] * nums[startPointer];
            int endSquared = nums[endPointer] * nums[endPointer];
            if (startSquared > endSquared) {
                ans[ansPointer] = startSquared;
                startPointer++;
            } else {
                ans[ansPointer] = endSquared;
                endPointer--;
            }
            ansPointer--;
        }
        
        return ans;
    }
};