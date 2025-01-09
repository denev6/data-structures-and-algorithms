# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        # head will keep pointing the head of the list.
        # node will move forward to link new nodes.
        # To do this, init a empty node.
        head = node = ListNode()

        while l1 or l2 or carry:

            n = carry
            if l1:
                n += l1.val
                l1 = l1.next
            if l2:
                n += l2.val
                l2 = l2.next

            # check if there's carry
            if n >= 10:
                n = n % 10
                carry = 1
            else:
                carry = 0

            # Link new a node
            node.next = ListNode(n)
            node = node.next

        return head.next
