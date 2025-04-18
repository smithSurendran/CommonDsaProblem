# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        #print(count)
        if count==n:
            return head.next
        for _ in range(count-n-1):
            curr= curr.next
        
        if curr.next:
            curr.next= curr.next.next

        return head

        