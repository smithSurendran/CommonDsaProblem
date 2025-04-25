# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeList(l1, l2):
            d =ListNode(0)
            m= d
            while l1 and l2:
                if l1.val<=l2.val:
                    m.next= l1
                    l1=l1.next
                else:
                    m.next=l2
                    l2=l2.next
                m=m.next
            if l2:
                m.next= l2
            if l1:
                m.next= l1
            l1=d.next
            return l1
        
        merge=lists[0]
        for i in range(1,len(lists)):
            
            merge= mergeList(merge, lists[i])
        
        return merge



            

            


