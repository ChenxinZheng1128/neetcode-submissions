class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagram_map;

        for (const string& s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            anagram_map[key].push_back(s);
        }

        vector<vector<string>> result;
        result.reserve(anagram_map.size());

        for (auto& [key, group] : anagram_map) {
            result.push_back(move(group));
        }

        return result;
    }
};
