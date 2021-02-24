# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        next_node = None
        prev_node = None
        cur_node = head
        while cur_node is not None: 
			# save the next node in a temp variable
            next_node = cur_node.next 
			
			# since we saved the next node, we can make the connection 
            cur_node.next = prev_node
			
			# save for next iteration
            prev_node = cur_node 
			
			# Assign to the current node from temp variable
            cur_node = next_node 
        
		    # At this point, the cur_node will be None, hence return the prev_node
        return prev_node

runtime O(n)
space O(1).
