class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def binary_to_decimal(head):
    decimal_value = 0
    current = head

    while current is not None:
        decimal_value = decimal_value * 2 + current.value
        current = current.next

    return decimal_value

# Example usage
# Create a linked list: 0 -> 1 -> 0 -> 0 -> 1 -> 1
linked_list = ListNode(0, ListNode(1, ListNode(0, ListNode(0, ListNode(1, ListNode(1)))))))

# Convert the linked list to decimal
decimal_result = binary_to_decimal(linked_list)

print(decimal_result)
