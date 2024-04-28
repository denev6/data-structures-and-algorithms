// Follow up: If you have figured out the O(n) solution, 
// try coding another solution of which the time complexity is O(n log(n)).

class Solution {
public:
    // Ref: solutions/59090/C++-O(n)-and-O(nlogn)
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int len = INT_MAX;
        
        vector<int> prefixSum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        
        /*
            let prefixSum: ps, target: t
            find min distance between i and j
            ps[i] - ps[j] >= t where i > j
            
            ps[i] - ps[j] >= t
            ps[i] - t >= ps[j]  --> line 25
        */
        for (int i = n; i >= 0 && prefixSum[i] >= target; i--) {
            int j = upper_bound(prefixSum.begin(), prefixSum.end(), prefixSum[i] - target) - prefixSum.begin();
            len = min(len, i - j + 1);
        }
        return len == INT_MAX ? 0 : len;
    }
};