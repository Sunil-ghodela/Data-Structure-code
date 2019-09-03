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



output =  [4, 2, 5, 1, 3]
root = None

def makeTreeByPath(inOrderPathArray):

    for dataIndex in range(len(inOrderPathArray)):


        def Maa():
            childRoot = None



        if root == None:
           root = Node(inOrderPathArray[dataIndex])
           root.left = None
           root.right = None
        

        else:
            if root.left and root.right == None:
                childRoot = Node(inOrderPathArray[dataIndex])
                childRoot.left = Node(root)
            elif root.left != None and root.right == None:
                childRoot = Node(inOrderPathArray[dataIndex])
                root.right = Node(childRoot)



            childRoot.left = Node(root)

        root = childRoot
             
        

        # if childRoot == None:
        #     childRoot = Node(inOrderPathArray[dataIndex]) #
        #     if root == None:
        #         childRoot.left = None
        #         childRoot.right = None
        #     else:
        #         childRoot.left = Node(root)

        # else:
        #     pass

        # root = Node(childRoot)
            


        root = Node(inOrderPathArray[dataIndex])
        if root.left == None:
            root.left

root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5)

printInorder(root)
# output: [4 2 5 1 3]

