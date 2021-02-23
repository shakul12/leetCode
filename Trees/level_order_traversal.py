def levelOrder(root):
	out=[]
	level=0
	if not root:
		return out
	temp= [root]
	while temp:
		ran=len(temp)
		out.append([])
		for i in range(ran):
			node=temp.pop(0)
			out[level].append(node.val)
			if node.left:
				temp.append(node.left)
			if node.right:
				temp.append(node.right)
		level+=1
	return out
