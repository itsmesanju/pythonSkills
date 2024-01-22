"""
We first find this number of operations to perform, then we use a loop that operates n times, 
such that anything to the right of our swap operations are untouched. 
This also neatly solves any null pointer exceptions as well.

Then, we use two pointers. They both start at the same position, 
one moves forward k times and appends all values to a stack, 
then we slide the other over k times to modify values by popping from the stack. 

Both pointers end up pointing to one position further than k, at the first index of the next node to modify.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        ptr = head
        head_ptr = head

        count = 0
        while(ptr != None):
            ptr = ptr.next
            count += 1
        
        times = count // k

        left = head
        right = head

        pos = 1
        q = deque()


        while(times > 0):
            dummy = left
            for i in range(0,k):
                print(left.val)
                q.append(left.val)
                left = left.next
            for i in range(0,k):
                dummy.val = q.pop()
                dummy = dummy.next
            left = dummy
            times -= 1
        return head_ptr
        

        
