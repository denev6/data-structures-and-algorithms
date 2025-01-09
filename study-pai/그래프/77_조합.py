class Solution:
    """use DFS with condition (ref. 46_순열)"""

    def combine(self, n: int, k: int):
        result = []

        def dfs(nodes, start):
            if len(nodes) == k:
                result.append(nodes[:])
                return  # do not move deeper

            for i in range(start, n + 1):
                nodes.append(i)
                dfs(nodes, i + 1)  # combination, not permutation.
                nodes.pop()

        dfs([], 1)
        return result


from itertools import combinations


class Solution2:
    def combine(self, n: int, k: int):
        ans = combinations(range(1, n + 1), k)
        # type of combination elements are tuple
        ans = map(lambda e: list(e), ans)
        return list(ans)


assert Solution().combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
assert Solution().combine(1, 1) == [[1]]
