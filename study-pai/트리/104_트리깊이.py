class MySolution:
    # Use DFS. 0ms
    def maxDepth(self, root) -> int:
        if root is None:
            return 0

        def dfs(node, depth):
            left_depth = right_depth = depth
            left = node.left
            right = node.right

            if left:
                left_depth = dfs(left, depth + 1)
            if right:
                right_depth = dfs(right, depth + 1)

            return max(left_depth, right_depth)

        return dfs(root, 1)


from collections import deque


class Solution:
    # Use BFS. 0ms
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        queue = deque([root])
        depth = 0

        while queue:
            depth += 1

            for _ in range(len(queue)):
                current_root = queue.popleft()
                if current_root.left:
                    queue.append(current_root.left)
                if current_root.right:
                    queue.append(current_root.right)

        return depth
