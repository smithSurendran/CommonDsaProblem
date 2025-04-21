# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow= fast= head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        mid= slow

        def rev(node):
            if node is None or node.next is None:
                return node
            new_head= rev(node.next)

            node.next.next= node
            node.next= None

            return new_head
        
        second= rev(mid)
        first= head
        while second.next:
            temp = first.next
            first.next=second
            first= temp

            temp=second.next
            second.next= first
            second=temp

        return head
             

        