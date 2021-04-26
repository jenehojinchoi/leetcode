# 19. Remove Nth Node From End of Linked List

# Approach 1. Find length 
# TC: O(L), SC: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0) 
        dummy.next = head
        length = 0
        first = head
        while first:
            length += 1
            first = first.next
        
        length -= n
        first = dummy 
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

# Approach 2. One-pass
# TC: O(L), SC: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n+1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next

        return dummy.next