from collections import deque


class TreeNode(object):
    pass


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        result = ["#"]
        # serialize using BFS
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                # represent "null" as "#"
                result.append("#")

        # separate values with space
        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "# #":
            return None

        data = data.split()[1:]
        root = TreeNode(int(data[0]))
        queue = deque([root])

        index = 1

        while queue:
            node = queue.popleft()
            if data[index] is not "#":
                node.left = TreeNode(int(data[index]))
                queue.append(node.left)
            index += 1

            if data[index] is not "#":
                node.right = TreeNode(int(data[index]))
                queue.append(node.right)
            index += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
