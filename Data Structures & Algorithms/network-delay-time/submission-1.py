class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        minHeap = [(0, k)]

        visited = {}

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue

            visited[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return max(visited.values()) if len(visited) == n else -1