class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minHeap = []

        for num, freq in count.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [i[1] for i in minHeap]