// Max Consecutive Ones

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ans = 0;
        int cnt = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i]) cnt++;
            if (!nums[i]) {
                ans = max(cnt, ans);
                cnt = 0;
            }
        }
        ans = max(ans, cnt);
        return ans;
    }
};