class Tree:
    def __init__(self, val):
        self.val=val
        self.word_finished= False
        self.children =[]
        self.count=1
class Solution:
    # @param A : list of strings
    # @return a list of strings
    def add(self,root, val):
        node=root
        for char in val:
            flag=True
            for child in node.children:
                if child.val==char:
                    child.count+=1
                    node=child
                    fag=False
                    break
            if flag:
                new_node= Tree(char)
                node.children.append(new_node)
                node=new_node
        node.word_finished=True
                
        
    def prefix(self, A):
        root= Tree('*')
        for a in A:
            self.add(root, a)
        out=[]
        for a in A:
            node=root
            for child in node.children:
                if child.val==a[0]:
                    node=child
                    break
            temp=''
            for char in a:
                temp+=char
                if node.count==1 and node.val!='*':
                    break
                for child in node.children:
                    if child.val==char:
                        node=child
                        break
            out.append(temp)
        return out
        
            
