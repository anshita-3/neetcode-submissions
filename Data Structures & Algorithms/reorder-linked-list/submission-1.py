# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head:
        #     return
        # nodes=[]
        # curr=head
        # while curr:
        #     nodes.append(curr)
        #     curr=curr.next 
        # left=0
        # right=len(nodes)-1
        # while left<right:
        #     nodes[left].next=nodes[right]
        #     left+=1
        #     if left==right:
        #         break
        #     nodes[right].next=nodes[left]
        #     right-=1
        # nodes[left].next=None

        if not head or not head.next:
            return
        last=head
        while last.next:
            last=last.next
        second_last=head
        while second_last.next.next:
            second_last=second_last.next
        second_last.next=None
        last.next=head.next
        head.next=last
        self.reorderList(last.next)


