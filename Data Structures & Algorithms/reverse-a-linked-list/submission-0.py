# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head
        
        node = head
        previous_node = None
        while node.next is not None:
            previous_node = ListNode(val=node.val, next=previous_node)
            node = node.next 

        node.next = previous_node
        return node