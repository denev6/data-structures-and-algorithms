class WrongSolution:
    """find Permutation, not Combination
    """

    def combinationSum(self, candidates, target):
        ans = []

        def dfs(path):
            if sum(path) == target:
                ans.append(path[:])
                return

            if sum(path) > target:
                path.pop()
                return

            for cand in candidates:
                next_node = path[:]
                next_node.append(cand)

                dfs(next_node)

        dfs([])
        return ans


class Solution:
    """pass 'index' parm to prevent accessing the previous candidate
    """

    def combinationSum(self, candidates, target):
        result = []

        def dfs(index, path):
            if sum(path) > target:
                return
            if sum(path) == target:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                candidate = candidates[i]
                next_path = path + [candidate]
                dfs(i, next_path)

        dfs(0, [])
        return result


assert Solution().combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]]
assert Solution().combinationSum(candidates=[2, 3, 5], target=8) == [
    [2, 2, 2, 2],
    [2, 3, 3],
    [3, 5],
]
