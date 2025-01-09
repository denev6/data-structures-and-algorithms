from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges):
        """Solution:
        1. draw a bi-directed graph
        2. remove leaf nodes (repeat)
        3. find the root nodes
        """

        if n <= 1:
            # Check test case below
            return [0]

        # bi-directed graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Find leaf nodes
        # if these's only one connection,
        # it means the node is a leaf.
        leaf_nodes = []
        for u in graph:
            if len(graph[u]) == 1:
                leaf_nodes.append(u)

        # Remove leaf nodes
        # Connected nodes can be the new leaf nodes in the next time step.
        # FYI, the connection between nodes are bi-directional
        while n > 2:
            n -= len(leaf_nodes)
            new_leaf_nodes = []

            for leaf in leaf_nodes:
                # remove connection
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaf_nodes.append(neighbor)

            leaf_nodes = new_leaf_nodes

        return leaf_nodes


# Test case
assert Solution().findMinHeightTrees(n=1, edges=[]) == [0]
