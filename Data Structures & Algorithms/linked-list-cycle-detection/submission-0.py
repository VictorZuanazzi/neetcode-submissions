# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Find cycle by reverting the linked list,
        # if the head appears twice, there is a cycle
        previous_node = None
        previous_head = head
        while head is not None:
            next_node = head.next
            head.next = previous_node
            previous_node = head
            head = next_node

            if previous_head == head:
                return True
        
        return False
        
