# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=None
        node= head
        p=None

        while node:

            dummy=node.next
            node.next= p
            p=node
            node=dummy
            

        return p