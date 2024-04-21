// Find Numbers with Even Number of Digits

class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < nums.size(); i++) {
            int item = nums[i];
            int base = 1;
            int numDigit = 1;
            
            for (int j = 0; j < 5; j++) {
                base *= 10;
                if (base > item) break;
                numDigit++;
            }
            if (numDigit % 2 == 0) ans++;
        }
        return ans;
    }
};