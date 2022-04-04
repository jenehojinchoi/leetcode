# 19. Remove Nth Node From End of Linked List

# Approach 1. Make a dummy node
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # until right reaches the end of the list
        while right:
            left = left.next
            right = right.next
            
        # delete
        left.next = left.next.next
        
        return dummy.next

'''
Runtime: 68 ms, faster than 9.94% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 23.01% of Python3 online submissions for Remove Nth Node From End of List.
'''

# Approach 2. No dummy node, stop when right.next = None
class Solution:
    def removeNthFromEnd(self, head, n):
        left = right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        if not right:
            return head.next
        
        # until right reaches None
        while right.next:
            left = left.next
            right = right.next
            
        # delete
        left.next = left.next.next
        
        return head