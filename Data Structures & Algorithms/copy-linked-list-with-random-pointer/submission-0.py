class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return
        hashmap={None:None}
        curr=head
        while curr:
            hashmap[curr]=Node(curr.val)
            curr=curr.next 
        curr=head
        while curr:
            copy=hashmap[curr]
            copy.next=hashmap[curr.next]
            copy.random=hashmap[curr.random]
            curr=curr.next 
        return hashmap[head]
