# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        left=dummy
        right=dummy
        for i in range(n+1):
            right=right.next
        while right:
            left=left.next
            right=right.next
        left.next=left.next.next
        return dummy.next
        # curr=head
        # length=0
        # while curr:
        #     length+=1
        #     curr=curr.next
        # if n==length:
        #     return head.next
        # curr=head
        # for i in range(length-n-1):
        #     curr=curr.next
        # curr.next=curr.next.next
        # return head