# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = head
        curr = prev.next
        while curr:
            next_node = curr.next
            if prev.val == curr.val:
                prev.next = next_node
            else:
                prev = curr
            curr = next_node
        return head
