"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode()  # Nodo centinela para simplificar
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

def list_to_linkedlist(nums):
    dummy = ListNode()
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Tests
def test_addTwoNumbers():
    l1 = list_to_linkedlist([2,4,3])
    l2 = list_to_linkedlist([5,6,4])
    result = addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [7,0,8], "Test case 1 failed"

    l1 = list_to_linkedlist([0])
    l2 = list_to_linkedlist([0])
    result = addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0], "Test case 2 failed"

    l1 = list_to_linkedlist([9,9,9,9,9,9,9])
    l2 = list_to_linkedlist([9,9,9,9])
    result = addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [8,9,9,9,0,0,0,1], "Test case 3 failed"

    print("Todos los tests pasaron correctamente.")

test_addTwoNumbers()