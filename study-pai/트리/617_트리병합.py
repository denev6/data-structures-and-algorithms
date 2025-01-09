class TreeNode:
    pass


class Solution:
    def mergeTrees(self, root1, root2):
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else:
            # return A or B
            # if both A and B are True: return A.
            # if both A and B are False: return B. --> which is always None in this case.
            # if only A or B is True: return the one is True.
            return root1 or root2
