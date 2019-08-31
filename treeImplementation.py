# tree implementation 

class Tree():

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


leftNode = Tree(10)
rightNode = Tree(20)

t = Tree(30, left= leftNode, right=rightNode)

print(t.left)
