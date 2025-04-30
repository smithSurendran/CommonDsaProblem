# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node= node.next
        
        dummy=ListNode(-1)
        merge= dummy
        while heap:
            merge.next=ListNode(heapq.heappop(heap))
            merge= merge.next
        return dummy.next 