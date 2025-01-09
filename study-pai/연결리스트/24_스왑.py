# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    def swapPairs(self, head):
        root = head

        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next

        return root


# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)


class Solution:
    def swapPairs(self, head):
        # root: pointing the head of list (to return the first node of list).
        root = prev = ListNode()
        prev.next = head

        while head and head.next:
            next = head.next  # tmp

            # swap
            head.next = head.next.next
            next.next = head
            prev.next = next

            # move forward
            prev = prev.next.next
            head = prev.next

        return root.next
