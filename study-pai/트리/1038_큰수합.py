class TreeNode:
    pass


class MySolution:
    def bstToGst(self, root):
        def dfs(node, larger_sum):
            val = node.val

            if node.right:
                larger_sum = dfs(node.right, larger_sum)
            larger_sum = val + larger_sum
            node.val = larger_sum

            if node.left:
                larger_sum = dfs(node.left, larger_sum)

            return larger_sum

        dfs(root, 0)
        return root


class Solution:
    larger_sum = 0

    def bstToGst(self, node):
        if node:
            self.bstToGst(node.right)
            self.larger_sum += node.val
            node.val = self.larger_sum
            self.bstToGst(node.left)

        return node
