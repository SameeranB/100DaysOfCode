# Day 4 - 15th August 2020
# This question was solved on leetcode: Question Number - 21

# The Question:

# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.


# Runtime - 44 ms - Faster than 44.59%
# Memory - 13.8 MB - Less than 75.17%



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = []
        
        while l1 != None or l2 != None:
            if l1 == None:
                while l2 != None:
                    output.append(ListNode(l2.val))
                    l2=l2.next
                
            elif l2 == None:
                while l1 != None:
                    output.append(ListNode(l1.val))
                    l1=l1.next
                    
            elif l1.val == l2.val:
                output.append(ListNode(val=l1.val))
                output.append(ListNode(val=l2.val))
                l1 = l1.next
                l2 = l2.next
            
            elif l1.val < l2.val:
                output.append(ListNode(val=l1.val))
                l1 = l1.next
                
            elif l1.val > l2.val:
                output.append(ListNode(l2.val))
                l2=l2.next
            
                    
        
        for i in range(len(output)-1):
            output[i].next = output[i+1]
        
        if len(output)>0:
            return output[0]
        else:
            return l1 if l2 == None else l2
