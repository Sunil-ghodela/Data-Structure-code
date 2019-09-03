# isTreeIsBinary?.py

								 
class getNode: 

	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def isFullBinaryTree( root) : 

	# if tree is empty 
	if (not root) : 
		return True

	q = [] 

	q.append(root) 

	while (not len(q)): 
		
		node = q[0] 
		q.pop(0) 

		# if it is a leaf node then continue 
		if (node.left == None and
			node.right == None): 
			continue

		if (node.left == None or
			node.right == None): 
			return False

		q.append(node.left) 
		q.append(node.right) 
	
	return True

# Driver Code 
if __name__ == '__main__': 
	root = getNode(1) 
	root.left = getNode(2) 
	root.right = getNode(3) 
	root.left.left = getNode(4) 
	root.left.right = getNode(5) 

	if (isFullBinaryTree(root)) : 
		print("Yes" ) 
	else: 
		print("No") 