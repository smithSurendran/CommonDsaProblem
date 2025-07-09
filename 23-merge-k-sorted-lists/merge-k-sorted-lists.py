# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result=[]
        for li in lists:
            while li:
                result.append(li.val)
                li= li.next
        print(result)
        result= sorted(result)
        dummy= ListNode()
        current= dummy
        for num in result:
            current.next=ListNode(num)
            current= current.next
        return dummy.next

