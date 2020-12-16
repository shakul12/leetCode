# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def scanner(self, final,A):
        while len(A)>0:
            mini=99999
            target=None
            l=len(A)
            for i in range(l):
                try:
                    if A[i].val<mini:
                        mini=A[i].val
                        target=i
                except:
                    pass
            node= ListNode(mini)
            final.next=node
            final=final.next
            A[target]=A[target].next
            A= [x for x in A if x!=None]
        #return final
            
    def mergeKLists(self, A):
        if len(A)==1:
            return A[0]
        mini=99999
        target=None
        for i in range(len(A)):
            if A[i].val<mini:
                mini=A[i].val
                target=i
        final= ListNode(mini)
        A[target]=A[target].next
        
        self.scanner(final, A)
        return final