class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count_map;
        for (int num : nums) {
            count_map[num]++;
        }

        vector<vector<int>> buckets(nums.size() + 1);
        for (auto& [num, freq] : count_map) {
            buckets[freq].push_back(num);
        }

        vector<int> result;
        result.reserve(k);

        for (int i = buckets.size() - 1; i >= 0; --i) {
            for (int num : buckets[i]) {
                result.push_back(num);
                if (result.size() == k) {
                    return result;
                }
            }
        }
        return result;
    }
};
