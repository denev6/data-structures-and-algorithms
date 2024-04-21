// Third Maximum Number
// Follow up: Can you find an O(n) solution?

#include<cmath>

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long min = pow(-2, 31) - 1;  // 문제 조건: -2^31 <= nums[i] <= 2^31 - 1
        long third = min, second = min, first = min;
        
        for (auto n : nums) {
            if (n > first) {
                third = second;
                second = first;
                first = n;
            } else if  (second < n && n < first) {
                third = second;
                second = n;
            } else if (third < n && n < second) {
                third = n;
            }
        }
        if (third == min) {
            return first;
        }
        return third;
    }
};