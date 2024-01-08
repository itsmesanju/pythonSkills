# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      """
      Approach:

      Traverse the linked list and continue adding all addresses in the list. If any address is in visited list, return True.
      """
       address=[]

       while head is not None:
           address.append(head)
           head = head.next
           if head in address:
               return True
       return False 
