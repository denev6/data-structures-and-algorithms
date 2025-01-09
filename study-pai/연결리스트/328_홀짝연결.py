# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        if head is None:
            # If not, AttributeError: 
            # 'NoneType' object has no attribute 'next'.
            return head
        
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            # Link odd to odd and even to even.
            odd.next = even.next
            even.next = even.next.next

            # move forward
            odd = odd.next
            even = even.next
        
        odd.next = even_head
        return head
