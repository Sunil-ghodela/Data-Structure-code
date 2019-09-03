# InOrder Traverse in A Tree
#  Root---> Left----> Right

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

# A function to do inorder tree traversal 
def printInorder(root):
    # root = 
    #         1
    #       2-----3
    #     4---5
    if root:
        print(root.val)

        printInorder(root.left)
        
        printInorder(root.right) 
  
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5)

printInorder(root)
# output: [1 2 4 5 3]

