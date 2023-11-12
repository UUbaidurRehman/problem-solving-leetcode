# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # M2: fast/slow pointer , reverse first/second half , compare two halves
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = slow
        slow = slow.next
        prev.next = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        fast , slow = head , prev
        while slow :
            if fast.val != slow.val:    return False
            fast, slow = fast.next, slow.next
        return True
        

