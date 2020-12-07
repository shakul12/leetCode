# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        stack= []
        head=A
        count=1
        while A:
            if count%2==0:
                stack.append(A.val)
                A.val=None
            count+=1
            A=A.next
        A=head
        while A:
            if A.val==None:
                A.val=stack.pop()
            A=A.next
        return head