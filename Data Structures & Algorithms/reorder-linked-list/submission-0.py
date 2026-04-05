# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow=head,head
        if not head or not head.next:
            return 
        while fast!=None and fast.next!=None:
            fast=fast.next.next 
            slow=slow.next 
        #starting second haf
        second=slow.next 
        slow.next=None 
        prev=None
        curr=second
        nxt=None
        while curr!=None:
            nxt=curr.next 
            curr.next=prev
            prev=curr
            curr=nxt
        first, second = head, prev
        while second:
            nxt1,nxt2=first.next,second.next 
            first.next=second
            second.next=nxt1
            first, second = nxt1,nxt2

        




        