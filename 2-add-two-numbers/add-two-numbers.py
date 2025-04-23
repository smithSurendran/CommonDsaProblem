# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverseList(node):
            if node is None or node.next is None:
                return node
            
            new_head= reverseList(node.next)

            node.next.next= node
            node.next= None

            return new_head

        carry=0
        dummy= ListNode(0)
        new_node= dummy
        num1= l1
        num2= l2
        while num1 or num2 or carry:
            val1= num1.val if num1 else 0
            val2= num2.val  if num2 else 0

            total = val1+val2+carry
            carry=total//10
            new_node.next=ListNode(total%10)

            new_node= new_node.next
            if num1:
                num1=num1.next
            if num2:
                num2=num2.next
        print(new_node)
        print(dummy)

        #rev_num=reverseList(dummy.next)
        #print(rev_num)
        return dummy.next
        

        