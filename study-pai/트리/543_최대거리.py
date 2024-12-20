class MySolution:
    max_distance = 0

    def diameterOfBinaryTree(self, root) -> int:
        def dfs(node, depth):
            left_depth = right_depth = depth
            left = node.left
            right = node.right

            if left:
                left_depth = dfs(left, depth + 1)
            if right:
                right_depth = dfs(right, depth + 1)

            # distance: sum of relative depths from left and right
            # --> (left_depth - depth) + (right_depth - depth)
            distance = left_depth + right_depth - 2 * depth
            self.max_distance = max(self.max_distance, distance)

            # return max depth to root
            return max(left_depth, right_depth)

        dfs(root, 0)
        return self.max_distance


class Solution:
    longest = 0

    def diameterOfBinaryTree(self, root) -> int:
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            distance = left + right
            self.longest = max(self.longest, distance)

            return max(left, right) + 1

        dfs(root)
        return self.longest
