# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if (not list1) or (list2 and list1.val > list2.val):
            # if list2 is smaller, merge it to list1.
            list1, list2 = list2, list1
        if list1:
            # if list1 is smaller, continue.
            list1.next = self.mergeTwoLists(list1.next, list2)
            
        # if both list1 and list2 are None, return.
        return list1

            