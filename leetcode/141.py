# 141. Linked List Cycle

# Approach 1. Brute and Force: Store seen nodes
class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        seen = []
        while head:
            if head in seen:
                return True
            seen.append(head)
            head = head.next
        return False

# Approach 2. Fast and Slow
# If fast and slow reach at the same point, it'll mean that head has a cycle.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

