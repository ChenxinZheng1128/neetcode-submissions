import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for x in nums:
            if not sub or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect.bisect_left(sub, x)
                sub[idx] = x

        return len(sub)