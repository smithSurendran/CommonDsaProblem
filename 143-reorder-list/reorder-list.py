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
            if node is None or node.next is None:
                return node
            
            new_head= reverseList(node.next)

            node.next.next= node
            node.next= None

            return new_head
        
        fast=slow=curr=head

        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        rev_lst= reverseList(slow)
        merge= ListNode(-1)
        dummy= merge
        
        while rev_lst.next:
            temp= curr.next
            curr.next=rev_lst
            curr= temp

            temp= rev_lst.next
            rev_lst.next=curr
            rev_lst=temp

        print(merge)

    
        