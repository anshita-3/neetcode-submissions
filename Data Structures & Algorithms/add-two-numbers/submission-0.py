# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        carry=0
        while l1 or l2:
            if l1 and not l2:
                sum=l1.val+carry
                l1=l1.next
            elif not l1 and l2:
                sum=l2.val+carry
                l2=l2.next
            else:
                sum=l1.val+l2.val+carry
                l1=l1.next
                l2=l2.next
            digit=sum%10
            carry=sum//10
            res.append(digit)
        if carry:
            res.append(carry)
        
        dummy=ListNode(0)
        curr=dummy
        for num in res:
            curr.next=ListNode(num)
            curr=curr.next
        return dummy.next

        
        
            
        


        
            
            

