from collections import defaultdict


class Solution:  # For understanding
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # check if the graph is recurrent.
        graph = defaultdict(list)
        for after, before in prerequisites:
            graph[before].append(after)

        traced = set()

        def dfs(before):
            if before in traced:
                return False
            traced.add(before)

            # visit nodes with DFS
            while graph[before]:
                after = graph[before].pop()
                if not dfs(after):
                    return False

            # remove visited node for the next visit
            traced.remove(before)
            return True

        # check nodes one by one
        for before in list(graph):
            if not dfs(before):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = defaultdict(list)
        for after, before in prerequisites:
            graph[before].append(after)

        traced = set()
        visited = set()

        def dfs(before):
            if before in traced:
                return False
            if before in visited:
                # do not visit again
                return True

            traced.add(before)

            while graph[before]:
                after = graph[before].pop()
                if not dfs(after):
                    return False

            visited.add(before)
            traced.remove(before)
            return True

        for before in list(graph):
            if not dfs(before):
                return False
        return True


assert Solution().canFinish(2, [[1, 0]]) is True
assert Solution().canFinish(2, [[1, 0], [0, 1]]) is False
