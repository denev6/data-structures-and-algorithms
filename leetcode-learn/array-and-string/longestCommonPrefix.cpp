class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int prefixIdx = 201;
        for (int i = 1; i < strs.size(); i++) {
            string a = strs[i - 1];
            string b = strs[i];
            int common = 0;
            for (int j = 0; j < min(a.size(), b.size()); j++) {
                if (a[j] != b[j]) break;
                common++;
            }
            prefixIdx = min(prefixIdx, common);
        }
        return strs[0].substr(0, prefixIdx);
    }
};