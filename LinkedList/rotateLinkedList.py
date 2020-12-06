# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        ll_len=0
        temp=A
        while temp:
            ll_len+=1
            temp= temp.next    
        if ll_len==1:
            return A
        if B>ll_len:
            B= B%ll_len
            if B==0:
                return A
        ll_len=ll_len-B
        head=A
        while ll_len>1:
            A=A.next
            ll_len-=1
        temp=A.next
        A.next=None
        out_head=temp
        while temp.next:
            temp=temp.next
        temp.next=head
        return out_head
        