# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        root = prev = ListNode()
        root.next = head

        # move to the point where we need to swap
        # head is the first node need to be swapped.
        for _ in range(left - 1):
            prev = prev.next
        head = prev.next

        for _ in range(right - left):
            tmp = head.next
            head.next = head.next.next
            tmp.next = prev.next
            prev.next = tmp

        return root.next
