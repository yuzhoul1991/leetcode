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
    ListNode *detectCycle(ListNode *head) {
        // Easy solution with unordered_set
        unordered_set<ListNode*> set;
        while(head) {
            if(set.find(head) != set.end())
                return head;
            set.insert(head);
            head = head->next;
        }
        return NULL;
    }
};
