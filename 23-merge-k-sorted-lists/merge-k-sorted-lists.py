# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for node in lists:
            while node:
                arr.append(node.val)
                node= node.next
        
        arr= sorted(arr)
        dummy= ListNode(0)
        merge=dummy
        for num in arr:
            merge.next=ListNode(num)
            merge=merge.next
        return dummy.next

