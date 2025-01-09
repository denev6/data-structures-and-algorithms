"""
**heapq: Min Heap, Priority Queue**

heapq.heappush(heap, item)
heapq.heappop(heap)
heapq.heapify(x): O(N)
"""

import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        root = result = ListNode(None)  # to point the first node
        heap = []  # init PriorityQueue

        for i in range(len(lists)):
            if lists[i]:
                head = (lists[i].val, i, lists[i])  # (value, list index, node)
                # If there is equal item in heapq, it raises
                # TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
                # To prevent TypeError, add "list index" to identify each item.
                heapq.heappush(heap, head)  # push heads of lists

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                item = (result.next.val, idx, result.next)  # (value, list index, node)
                heapq.heappush(heap, item)

        return root.next
