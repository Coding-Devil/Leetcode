# Assuming ListNode is defined as:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()  # Placeholder for the result linked list
        current = dummy  # Pointer to build the new list
        carry = 0  # To store the carry

        # Loop until both lists are exhausted and there is no carry
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Value from l1 or 0 if l1 is None
            val2 = l2.val if l2 else 0  # Value from l2 or 0 if l2 is None

            # Calculate the sum of values and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Update the carry
            new_val = total % 10  # Determine the digit to store in the node

            # Move to the next node in both lists if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            # Append the new node to the result list
            current.next = ListNode(new_val)
            current = current.next

        return dummy.next