class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(nums: List[int]) -> ListNode:
    dummy = ListNode()
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next

def linkedlist_to_list(node: ListNode) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def print_linkedlist(node: ListNode) -> None:
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(" -> ".join(vals))
