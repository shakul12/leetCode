def zig_zag_traversal(root):
	out=[]
	direction=True
	temp=[]
	if not root:
		return out
	curr=[root,None]
	while curr:
		node= curr.pop(0)
		if node:
			if direction:
				temp.append(node.val)
			else:
				temp=[node.val]+temp
		else:
			out.append(temp)
			temp=[]
			if len(curr)>0:
				curr.append(None)
			direction= not direction
	return out
