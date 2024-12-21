class MySolution:
    def invertTree(self, root):
        if not root:
            return root

        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            node.left, node.right = node.right, node.left

        dfs(root)
        return root


class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(
                root.left
            )
            return root
        return None
