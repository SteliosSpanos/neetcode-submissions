class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, cst in flights:
            adj[s].append((d, cst))

        dist = [[float('inf')] * (k + 5) for _ in range(n)]
        dist[src][0] = 0
        minHeap = [(0, src, -1)]
        while len(minHeap):
            cst, node, stops = heapq.heappop(minHeap)
            if dst == node:
                return cst
            if stops == k or dist[node][stops + 1] < cst:
                continue

            for nei, w in adj[node]:
                nextCst = cst + w
                nextStops = 1 + stops
                if dist[nei][nextStops + 1] > nextCst:
                    dist[nei][nextStops + 1] = nextCst
                    heapq.heappush(minHeap, (nextCst, nei, nextStops))
        return -1
        