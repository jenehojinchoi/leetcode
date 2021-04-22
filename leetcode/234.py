# 234. Palindrome Linked List  

# Approach 1.
# TC: O(n), SC: O(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        visited = []
        while head:
            visited.append(head.val)
            head = head.next
        for i in range(len(visited)//2):
            if visited[i] != visited[len(visited)-1-i]:
                return False
        return True

# Approach 2. 
# TC: O(n), SC: O(1)
class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # slow = 2nd half
        # reverse it
        prev = None
        while slow:
            slow.next,slow,prev = prev,slow.next,slow

        # prev = reversed 2nd half
        first = head
        second = prev
        while first and second:
            if first.val!=second.val:
                return False
            first, second = first.next, second.next
        return True