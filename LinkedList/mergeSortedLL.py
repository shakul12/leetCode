# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        out_list=ListNode(0)
        curr= out_list
        
        while A and B:
            if A.val<B.val:
                curr.next=A
                A=A.next
            else:
                curr.next= B
                B=B.next
            curr= curr.next
        if A:
            curr.next= A
        else:
            curr.next=B
        return out_list.next
        