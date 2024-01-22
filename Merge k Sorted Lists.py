# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val

#         self.next = next

"""
The algorithm merges k sorted linked lists into a single sorted linked list using a min heap. 

It iterates through each linked list, pushing tuples of the form (value, count, node) onto the min heap. 

The min heap helps efficiently select the smallest element among the heads of the k lists. 
The merged linked list is constructed by repeatedly popping the smallest element from the heap and connecting the nodes. The algorithm maintains the order of insertion using a counter (cnt). 

The cnt (count) variable is used to maintain the order of insertion when nodes with the same values are encountered. 
In the min heap, if two nodes have the same value, the heap will compare their counts to determine the order.

The final result is the merged sorted linked list.
"""
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        dummy = ListNode(float('-inf'))
        curr = dummy
        cnt = 0

        for ll in lists:
            if ll :
                heappush(min_heap, (ll.val, cnt , ll))
                cnt += 1
        
        while min_heap:
            tmp_val, tmp_cnt, node = heappop(min_heap)
            curr.next = node
            if node.next:
                heappush(min_heap, (node.next.val, cnt ,node.next))
            curr = curr.next
            cnt += 1
        
        return dummy.next
