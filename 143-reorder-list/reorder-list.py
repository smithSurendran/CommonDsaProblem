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
        def reverseList(node):
            if not node or node.next is None:
                return node
            
            new_head= reverseList(node.next)

            node.next.next= node
            node.next= None

            return new_head
        
        slow= fast= head

        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        
        mid= slow
        revList= reverseList(mid)

        curr= head

        while revList.next:
            temp= curr.next
            curr.next= revList
            curr= temp

            temp=revList.next
            revList.next= curr
            revList= temp
        return head
             

        