class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Example usage:
# Construct a sample linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Reverse the linked list
new_head = reverse_linked_list(head)

# Print the reversed linked list
while new_head is not None:
    print(new_head.value, end=" ")
    new_head = new_head.next
