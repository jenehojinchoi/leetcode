# 203. Remove Linked List Elements

# Approach 1. String operations
class Solution:
    def removeElements(self, head, val):
        while head and head.val == val: 
            head = head.next 
            if not head: 
                return head
                
        next_node = head 
        while next_node and next_node.next:
            if next_node.next.val == val: 
                next_node.next = next_node.next.next 
            else: 
                next_node = next_node.next 
        return head

# Approach 2. Using dummy, next
class Solution:
    def removeElements(self, head, val): 
        result = ListNode(-1)
        result.next = head
        temp = result

        while temp != None and temp.next != None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return result.next