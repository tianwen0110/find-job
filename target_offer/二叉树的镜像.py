'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def mirror(self, tree):
        if tree == None:
            return None
        tree1 = TreeNode(tree.val)
        tree1.left = self.mirror(tree.right)
        tree1.right = self.mirror(tree.left)
        return tree1

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

s = solution()
tree = s.mirror(pNode1)
print(tree.left.left.val)
print(tree.left.right.val)