class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(node):
            if node is None:
                # leaf node
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left is False or right is False:
                # Keep returning False if subtree is not balanced.
                return False

            diff = abs(left - right)
            if diff > 1:
                # Current subtree is not balanced.
                return False

            # depth of subtree
            depth = max(left, right) + 1
            return depth

        return dfs(root) is not False
