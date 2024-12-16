from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, weight in times:
            # weight(delay time) of u -> v
            graph[u].append((v, weight))

        # queue: [ (delay_time, destination), ]
        queue = [(0, k)]
        # dist: { destination: weight }
        dist = {}

        while queue:
            time, node = heapq.heappop(queue)
            if node not in dist:
                dist[node] = (
                    time  # store the smallest weight computed from the previous step
                )

                # dijkstra
                for v, weight in graph[node]:
                    # visit adjacent nodes from "node" to "v"
                    delay_time = time + weight
                    heapq.heappush(queue, (delay_time, v))
            # else(:node in dist) means the node is already considered.
            # == The smallest weight is already marked in "dist".
            # FYI, we push all the cases(weights) in the priority queue.
            # i.e. [(5, v), (3, v), (9, v), ... ]
            # In this case, the smallest weights will be pop at first. (i.e. (3, v))
            # So, we can ignore other larger weights. (i.e. (5, v), (9, v))

        if len(dist) == n:
            # Check if all the nodes are visited.
            return max(dist.values())
        return -1


assert (
    Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2) == 2
)
assert Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=1) == 1
assert Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=2) == -1
