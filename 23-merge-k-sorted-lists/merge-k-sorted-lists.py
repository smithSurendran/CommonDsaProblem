# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap=[]
        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, id(l), l))
        
        dummy= ListNode()
        current= dummy

        while min_heap:
            _, _, node= heapq.heappop(min_heap)
            
            current.next= node
            current= current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val,id(node.next),node.next))
        return dummy.next

