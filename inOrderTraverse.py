# InOrder Traverse in A Tree
#  Left---> Root----> Right

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
        printInorder(root.left) 
        print(root.val)
        printInorder(root.right) 
  
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5)

printInorder(root)
# output: [4 2 5 1 3]

