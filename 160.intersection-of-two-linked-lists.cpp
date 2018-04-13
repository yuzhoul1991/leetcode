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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        unordered_set<int> set;
        while(headA) {
            set.insert(headA->val);
            headA = headA->next;
        }
        while(headB) {
            if(set.find(headB->val) != set.end())
                return headB;
            headB = headB->next;
        }
        return NULL;
    }
};
