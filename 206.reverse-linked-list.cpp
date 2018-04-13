/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // recursive solution       
        if(!head or !head->next) return head;
        // Assume originally it is 1->2->3
        ListNode* head_of_rest_reversed = reverseList(head->next);
        // At this moment it is 1->2<-3
        head->next->next = head;
        head->next = NULL;
        return head_of_rest_reversed;
    }
};
