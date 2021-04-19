# 206. Reverse Linked List

# Approach 1. Iterative
# TC: O(n), SC: O(1)
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Approach 2. Recursive
# TC: O(n), SC: O(n)
class Solution:
    def reverseList(self, head):
        if not head or not head.next: 
            return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp

