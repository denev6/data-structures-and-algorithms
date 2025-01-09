class TreeNode:
    pass


class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            # First item of preorder is the root node.
            index = inorder.index(preorder.pop(0))

            # This root node is able to divide inorder to two subtrees.
            node = TreeNode(inorder[index])
            # First item is popped, so the next item is the root of left subtree.
            node.left = self.buildTree(preorder, inorder[0:index])
            # And so on...
            node.right = self.buildTree(preorder, inorder[index + 1 :])

            return node
