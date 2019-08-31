# tree implementation 

class Tree():

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


    def __iter__(self):
        if self.left != None:
            for data in self.left:
                yield data
        
        yield self.data

        if self.right  != None:
            for data in self.right:
                yield data

leftNode = Tree(10)
rightNode = Tree(20)
t1 = Tree(30, left= leftNode, right=rightNode)

leftNode = Tree(40)
leftNode = Tree(50)
t2 = Tree(60, left=leftNode, right=rightNode)

rootTree = Tree(70, left=t1, right=t2)



# traverse with Inorder logic...
def printInorder(root): 
    if root: 
        printInorder(root.left) 
        print(root.val)
        printInorder(root.right) 

print(printInorder(rootTree))