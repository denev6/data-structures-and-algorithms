# Understand DFS


class Solution:
    """
    Visualize "current_node":
    null -> 1 -> 12 -> 123
              -> 13 -> 132
         -> 2 -> 21 -> 213
              -> 23 -> 231
         -> 3 -> 31 -> 312
              -> 32 -> 321
    """

    def permute(self, nums):
        results = []  # leaf nodes
        current_node = []

        def dfs(to_visit):
            if len(to_visit) == 0:
                # when leaf node
                results.append(current_node[:])

            for num in to_visit:
                to_visit_next = to_visit[:]  # deepcopy
                to_visit_next.remove(num)

                current_node.append(num)  # one depth down. i.e. [1] -> [1, 2]
                dfs(to_visit_next)
                current_node.pop()  # one depth up. i.e. [1, 2] -> [1]

        dfs(nums)
        return results


assert Solution().permute([1, 2, 3]) == [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
]
assert Solution().permute([1]) == [[1]]
