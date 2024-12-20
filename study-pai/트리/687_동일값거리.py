class Solution:
    # derived from 543
    longest = 0

    def longestUnivaluePath(self, root) -> int:
        def dfs(node):
            if not node:
                return 0

            val = node.val
            left = node.left
            right = node.right

            left_depth = dfs(left)
            right_depth = dfs(right)

            # depth + 1 if val is equal (move deeper)
            # or init depth to 0 (count from current node)
            if left and left.val == val:
                left_depth += 1
            else:
                left_depth = 0

            if right and right.val == val:
                right_depth += 1
            else:
                right_depth = 0

            distance = left_depth + right_depth
            self.longest = max(self.longest, distance)

            return max(left_depth, right_depth)

        dfs(root)
        return self.longest
