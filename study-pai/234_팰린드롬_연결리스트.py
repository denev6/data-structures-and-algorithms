class MySolution:
    def isPalindrome(self, head) -> bool:
        # Turn Linked List into List.
        vals = list()
        node = head

        while node is not None:
            vals.append(node.val)
            node = node.next
        
        # check palindrome
        left_pointer = 0
        right_pointer = len(vals) - 1
        while left_pointer < right_pointer:
            if vals[left_pointer] != vals[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True
    
class Solution:
    def isPalindrome(self, head) -> bool:
        """
        Make a reversed linked list and compare.
        
        * slow runner: move 1 step at once
        * fast runner: move 2 steps at once
        """
        rev = None
        slow = fast = head
        while fast and fast.next:
            # fast runner moves 2 steps at once.
            # So, when fast runner arrives at the end,
            # slow runner moves will reach the middle of linked list.
            # That's all.
            fast = fast.next.next 

            # Make a reversed linked list.
            # if head: [1 2 3 2 1]
            # rev will be [2 1]
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev