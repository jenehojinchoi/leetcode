// 160. Intersection of Two Linked Lists

#include <iostream>
#include <set>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// 1. Brute And Force: TC: O(n*m), SC: O(1)
// class Solution {
// public:
//     ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
//         ListNode* currA = headA;
//         while (currA) {
//             ListNode* currB = headB;
//             while (currB) {
//                 if (currA == currB) {
//                     return currA;
//                 }
//                 currB = currB->next;
//             }
//             currA = currA->next;
//         }
//         return NULL;
//     }
// };

// 2. My solution: TC: O(n)
// class Solution {
// public:
//     ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
//         ListNode* currA = headA;
//         ListNode* currB = headB;
//         while (currA  && currB) {
//             if (currA == currB)
//                 return currA;
//             currA = currA->next;
//             currB = currB->next;
//             if (!currA && !currB)
//                 return NULL;
//             if (!currA) 
//                 currA = headB;
//             if (!currB)
//                 currB = headA;
//         }
//         return NULL;
//     }
// };

// 3. 
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        set<ListNode *> nodes_in_B;

        while (headB != nullptr) {        
            nodes_in_B.insert(headB);
            headB = headB->next;
        }

        while (headA != nullptr) {

            if (nodes_in_B.find(headA) != nodes_in_B.end()) {
                return headA;
            }
            headA = headA->next;
        }

        return nullptr;
    }
};