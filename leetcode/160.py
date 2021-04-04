# 160. Intersection of Two Linked Lists

# Approach 1. Nexted while loop 
# Time Complexity: O(n*m) (worst), Space Complexity: O(1)
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if not headA or not headB:
#             return null
        
#         tempheadB = headB 
#         while headA:
#             while headB:
#                 if headA == headB:
#                     return headA
#                 headB = headB.next
#             headA = headA.next
#             headB = tempheadB

# Approach 2. set
# Time Complexity: O(n+m), Space Complexity: O(m) or O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        setB = set()

        while headB is not None:
            setB.add(headB)
            headB = headB.next

        while headA is not None:
            if headA in setB:
                return headA
            headA = headA.next

        return None

# Approach 3. two pointers
# Time Complexity: O(2(n+m)) ~= O(n+m), Space Complexity: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        
        return pA