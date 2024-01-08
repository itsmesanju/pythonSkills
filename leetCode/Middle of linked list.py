# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        """
        two points, one fast, one slow. for each iteration of a while loop, slow moves up by one:
            slow.next
            and fast, moves, twice as fast, for each iteration:

            fast = fast.next.next
        when fast hits the end of the list, you return slow because it will have gone exactly half way through the list.
        """

        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
  
          slow_pointer = head
          fast_pointer = head
  
          while fast_pointer and fast_pointer.next:
              slow_pointer = slow_pointer.next
              fast_pointer = fast_pointer.next.next
      
          print(slow_pointer, fast_pointer)
          return slow_pointer

        """ Alternative algorithm efficiently finds the middle node of a linked list by traversing it with two pointers. The mid_node pointer is updated only when the count is even, ensuring that it ends up pointing to the middle node when the traversal is complete."""

        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

            count = 1
            mid_node = head
            temp = head
            while temp != None:
                #print(f"Current Node: {temp}, Middle: {mid_node}")
                if count%2 == 0:
                    mid_node = mid_node.next
                temp = temp.next
                count += 1
            return mid_node
