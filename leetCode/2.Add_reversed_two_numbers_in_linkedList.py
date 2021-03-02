# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        
        #Initialize the new linklist and add a dummy pointer
        newLinkedList= ListNode(0)
        current=newLinkedList
        
        #Run loop only if l1 or l2  has some data
        while (l1 is not None or l2 is not None):

            #Check if L2 is none/blank/ no more elements. if none, use 0 to add.  
            if l1 is None:
                l1data= 0
            else:
                l1data=l1.val
            
            #Check if L2 is none/blank/ no more elements. if none, use 0 to add.
            if l2 is None:
                l2data= 0
            else:
                l2data=l2.val
            
            # Add the elemements and determine if carry is required.
            sumValue= l1data+l2data+carry
            
            if sumValue < 10:
                sumValue = sumValue 
                carry = 0
            else:
                sumValue = sumValue % 10
                carry = 1
        
            #Insert the data into the linked list.
            current.next =ListNode(sumValue)   #Add them sum to the value
            current = current.next #Move the pointer
            
            #Move the pointers of l1 and l2.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        #In the end of carry is still has some value, add it into the linkedlist.
        if carry:
            current.next = ListNode(carry)
            
        return newLinkedList.next
