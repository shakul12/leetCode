class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        diff=99999
        node= None
        if root:
            temp_diff= root.val- p.val
            if temp_diff>0:
                diff= min(diff, temp_diff)
                if diff ==temp_diff:
                    node= root
            l= self.inorderSuccessor(root.left, p)
            r= self.inorderSuccessor(root.right, p)
            if l is None and r is None:
                return node
            if l is None:
                comp= r
            elif r is None:
                comp=l 
            else:
                if l.val>r.val:
                    comp=r
                else:
                    comp=l
            if node is None:
                return comp
            else:
                if node.val>comp.val:
                    return comp
                else:
                    return node
