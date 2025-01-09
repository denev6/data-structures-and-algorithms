/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode* current = head;
        
        // dummy -> sorted list ...
        ListNode* dummy = new ListNode();
        
        while(current) {
            ListNode* prevNode = dummy;
            while (prevNode->next && prevNode->next->val < current->val) {
                prevNode = prevNode->next;
            }
            ListNode* nextNode = current->next; // tmp
            current->next = prevNode->next;
            prevNode->next = current;
            
            current = nextNode;
        }
        return dummy->next;
    }
    
};