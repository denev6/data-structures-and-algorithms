// Find All Numbers Disappeared in an Array
// Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        /* 숫자에 대응하는 인덱스는 음수로 변환
            idx = num - 1
            nums[idx] = -nums[idx]
        */
        for(int i = 0; i < n; i++){
            int idx = abs(nums[i]) - 1;
            nums[idx] = -abs(nums[idx]);
        }

        // 음수가 아닌 index만 채우기
        vector<int> ans;
        for(int i = 0; i < n; i++) {
            if(nums[i] > 0) {
                ans.push_back(i + 1);
            }
        }
        return ans;
    }
};