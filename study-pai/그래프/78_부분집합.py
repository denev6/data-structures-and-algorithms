class Solution:
    def subsets(self, nums):
        ans = []

        def dfs(index, path):
            ans.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return ans


################################################


def test_solution(input, answer):
    output = Solution().subsets(input)
    for item in answer:
        if item in output:
            output.remove(item)
        else:
            raise AssertionError
    if output:
        raise AssertionError


test_solution([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
test_solution([0], [[], [0]])
