# 203. Remove Linked List Elements

# Approach 1. One pointer
class Solution:
    def removeElements(self, head, val):
        while head and head.val == val: 
            head = head.next 

        if not head: 
            return head
                
        current = head 
        while current and current.next:
            if current.next.val == val: 
                current.next = current.next.next 
            else: 
                current = current.next 
        return head

# Approach 2. Two pointers
class Solution:
    def removeElements(self, head, val): 
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr 
            curr = curr.next
        return dummy.next
