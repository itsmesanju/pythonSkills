# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        The problem seems to involve reversing a linked list. The idea might be to iterate through the list, changing the direction of pointers to reverse the order of nodes.
	The approach involves traversing the given singly-linked list and reversing the direction of pointers to achieve the reversal of the list. It employs a two-pointer approach where prev and current pointers are utilized to reverse the links between nodes in the list iteratively.
        """
        if head == None or head.next == None:
            return head

        prev= None
        current = head

        print(f"Starting at Head: {current}")
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            print(f"Now=> Current: {current}")
        return prev
        

runtime O(n)
space O(1).
