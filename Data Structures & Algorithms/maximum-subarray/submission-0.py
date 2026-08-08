class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = res = nums[0]

        for x in nums[1:]:
            cur = max(x, cur + x)
            res = max(res, cur)
        
        return res