class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Dictionary to store { current_sum: count_of_ways }
        dp = {0: 1}
        
        for num in nums:
            next_dp = {}
            for current_sum, count in dp.items():
                # Option 1: Add '+'
                next_dp[current_sum + num] = next_dp.get(current_sum + num, 0) + count
                # Option 2: Add '-'
                next_dp[current_sum - num] = next_dp.get(current_sum - num, 0) + count
            dp = next_dp
            
        return dp.get(target, 0)
