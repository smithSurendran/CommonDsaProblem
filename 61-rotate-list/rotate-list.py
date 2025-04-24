# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        tail= head
        length=1
        while tail.next:
            tail= tail.next
            length+=1
        
        tail.next= head
        new_tail=head
        k= k%length
        steps=length-k
        for _ in range(steps-1):
            new_tail= new_tail.next
        #print(new_tail)
        new_head= new_tail.next
        new_tail.next=None

        return new_head
        

