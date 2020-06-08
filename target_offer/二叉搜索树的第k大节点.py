class treenode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class solution(object):
    def find(self, tree, k):
        a = self.zhongxu(tree)
        # if k >len(a):
        #     return None
        # else:
        return a
    def zhongxu(self, tree):
        if tree.left == None and tree.right == None:
            a = [tree.value]
            return a
        elif tree.left == None:
            a = [tree.value]
            b = self.zhongxu(tree.right)
            a.extend(b)
            return a
        elif tree.right == None:
            b = self.zhongxu(tree.left)
            a = [tree.value]
            b.extend(a)
            return b
        else:
            a = [tree.value]
            b1 = self.zhongxu(tree.left)
            b2 = self.zhongxu(tree.right)
            b1.extend(a)
            b1.extend(b2)
            return b1
    

tree1 = treenode(5)
tree2 = treenode(3)
tree3 = treenode(2)
tree4 = treenode(4)
tree5 = treenode(7)
tree6 = treenode(6)
tree7 = treenode(8)
tree1.left = tree2
tree1.right = tree5
tree2.left = tree3
tree2.right = tree4
tree5.left = tree6
tree5.right = tree7

s = solution()
print(s.find(tree1, 1))