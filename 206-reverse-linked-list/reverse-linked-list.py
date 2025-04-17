# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        # curr= head
        # prev= None

        # while curr:
        #     next_node= curr.next
        #     curr.next= prev
        #     prev= curr
        #     curr= next_node
        
        # return prev

        if head is None or head.next== None:
            return head
        
        new_head= self.reverseList(head.next)

        head.next.next= head
        head.next= None

        return new_head



        