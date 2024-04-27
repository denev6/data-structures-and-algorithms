class Solution {
public:
    // Ref: github.com/keineahnung2345/leetcode-cpp-practices
    string addBinary(string a, string b) {
        int lenStr = max(a.size(), b.size()) + 1;
        
        // zero padding
        a.insert(a.begin(), lenStr - a.size(), '0');
        b.insert(b.begin(), lenStr - b.size(), '0');

        // To iterate from i = 0
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        
        int i = 0, carry = 0;
        
        for(int i = 0; i < lenStr; i++){
            int intA = charToInt(a[i]);
            int intB = charToInt(b[i]);
            int sum = intA + intB + carry;
            
            switch(sum){
                case 3:
                    a[i] = '1';
                    carry = 1;
                    break;
                case 2:
                    a[i] = '0';
                    carry = 1;
                    break;
                case 1:
                    a[i] = '1';
                    carry = 0;
                    break;
            }
        }
        
        // recover reversed (+ trim left-zero)
        if(a[lenStr - 1] == '0') a.resize(lenStr - 1);
        reverse(a.begin(), a.end());
        return a;
    }
    
    int charToInt(char c) {
        return c - '0';
    }
};