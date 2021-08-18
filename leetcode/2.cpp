// 2. Add Two Numbers

#include <iostream>
// Definition for singly-linked list.
struct ListNode {
    int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* curr1 = l1;
        ListNode* curr2 = l2;
        
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        
        int carry = 0;
        while ((curr1!=nullptr) && (curr2!=nullptr)) {
            int sum = carry + curr1->val + curr2->val;
            carry = sum/10;
            curr->next = new ListNode(sum%10);
            curr = curr->next;
            curr1 = curr1->next;
            curr2 = curr2->next;
        }
        
        // 마지막 carry > 10 인 경우
        if (carry > 0) {
            curr->next = new ListNode(carry);
        }
        
        return dummy->next;
    }
};