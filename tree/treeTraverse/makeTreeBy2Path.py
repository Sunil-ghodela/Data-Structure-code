class Node: 

	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']


def buildTree(inOrder, preOrder):
    inStrt = 0
    lenInOrder = len(inOrder) 
	
    if inStrt > lenInOrder:
        return None
        
    tNode = Node(preOrder[inStrt])
    inStrt += 1
    
    if inStrt == lenInOrder : return tNode
        
    inIndex = search(inOrder, inStrt, lenInOrder, tNode.data) 
	

    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1) 
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, lenInOrder) 

    return tNode 

def search(arr, start, end, value): 
	for i in range(start, end + 1): 
		if arr[i] == value: 
			return i 

def printInorder(node): 
	if node is None: 
		return
	
	# first recur on left child 
	printInorder(node.left) 
	
	# then print the data of node 
	print node.data, 

	# now recur on right child 
	printInorder(node.right) 
	

inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preOrder = ['A', 'B', 'D', 'E', 'C', 'F'] 


root = buildTree(inOrder, preOrder) 


print "Inorder traversal of the constructed tree is"
printInorder(root) 

