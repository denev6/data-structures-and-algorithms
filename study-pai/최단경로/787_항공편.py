from typing import List

from collections import defaultdict
import heapq


class Solution:
    """Time Limit Exceeded on Case A (below)"""

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        queue = [(0, src, -1)]  # (price, destination, n of stopover)
        # If k == 1, it means you can visit 3 nodes. (i.e. 0 -> 1 -> 2)
        # So, I set n_stopover to -1.

        while queue:
            price, node, n_stopover = heapq.heappop(queue)
            if node == dst:
                return price

            if n_stopover < k:
                for v, weight in graph[node]:
                    new_price = price + weight
                    heapq.heappush(queue, (new_price, v, n_stopover + 1))

        return -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        queue = [(0, src, -1)]
        visited = set()

        while queue:
            price, node, n_stopover = heapq.heappop(queue)
            if node == dst:
                return price

            if (node, n_stopover) not in visited:
                # To prevent visiting the node with larger weight(price). --> time saving
                # FYI, even if the node has already been visited,
                # if the n_stop is different, it should be considered in a separate case(route).
                visited.add((node, n_stopover))

                if n_stopover < k:
                    for v, weight in graph[node]:
                        new_price = price + weight
                        heapq.heappush(queue, (new_price, v, n_stopover + 1))

        return -1


assert (
    Solution().findCheapestPrice(
        n=4,
        flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
        src=0,
        dst=3,
        k=1,
    )
    == 700
)
assert (
    Solution().findCheapestPrice(
        n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1
    )
    == 200
)
assert (
    Solution().findCheapestPrice(
        n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0
    )
    == 500
)
assert (
    Solution().findCheapestPrice(
        n=4, flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], src=0, dst=3, k=1
    )
    == 6
)

# Case A
assert (
    Solution().findCheapestPrice(
        n=13,
        flights=[
            [11, 12, 74],
            [1, 8, 91],
            [4, 6, 13],
            [7, 6, 39],
            [5, 12, 8],
            [0, 12, 54],
            [8, 4, 32],
            [0, 11, 4],
            [4, 0, 91],
            [11, 7, 64],
            [6, 3, 88],
            [8, 5, 80],
            [11, 10, 91],
            [10, 0, 60],
            [8, 7, 92],
            [12, 6, 78],
            [6, 2, 8],
            [4, 3, 54],
            [3, 11, 76],
            [3, 12, 23],
            [11, 6, 79],
            [6, 12, 36],
            [2, 11, 100],
            [2, 5, 49],
            [7, 0, 17],
            [5, 8, 95],
            [3, 9, 98],
            [8, 10, 61],
            [2, 12, 38],
            [5, 7, 58],
            [9, 4, 37],
            [8, 6, 79],
            [9, 0, 1],
            [2, 3, 12],
            [7, 10, 7],
            [12, 10, 52],
            [7, 2, 68],
            [12, 2, 100],
            [6, 9, 53],
            [7, 4, 90],
            [0, 5, 43],
            [11, 2, 52],
            [11, 8, 50],
            [12, 4, 38],
            [7, 9, 94],
            [2, 7, 38],
            [3, 7, 88],
            [9, 12, 20],
            [12, 0, 26],
            [10, 5, 38],
            [12, 8, 50],
            [0, 2, 77],
            [11, 0, 13],
            [9, 10, 76],
            [2, 6, 67],
            [5, 6, 34],
            [9, 7, 62],
            [5, 3, 67],
        ],
        src=10,
        dst=1,
        k=10,
    )
    == -1
)
