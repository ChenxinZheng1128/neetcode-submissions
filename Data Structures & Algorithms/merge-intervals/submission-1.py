class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = []
        res.append(intervals[0])

        for s, e in intervals[1:]:
            if s <= res[-1][1]:
                res[-1][1] = max(e, res[-1][1])
            else:
                res.append([s, e])

        return res
            

