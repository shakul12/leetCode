# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        head=A
        prev=A
        curr=A.next
        
        while curr:
            temp=prev.val
            prev.val=curr.val
            curr.val=temp
            prev= curr.next
            if curr.next:
                curr=curr.next.next
            else:
                curr=None
        return head