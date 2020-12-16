def flatten(self, A):
        if not A:
            return None
        curr=A
        while curr:
            if curr.left:
                left=curr.left
                while left.right:
                    left=left.right
                left.right=curr.right
                curr.right=curr.left
                curr.left=None
            curr=curr.right
        return A