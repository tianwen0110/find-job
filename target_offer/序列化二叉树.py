'''
请实现两个函数，分别用来序列化和反序列化二叉树。这里没有规定序列化的方式。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def order(self, tree):
        if tree == None:
            return ['#']
        if tree.left == None and tree.right == None:
            return [tree.val, '#', '#']
        if tree.left != None:
            list1 = [tree.val] + self.order(tree.left) 
        else:
            list1 = [tree.val, '#']
        if tree.right != None:
            list1 = list1 + self.order(tree.right) 
        else:
            list1 = list1 + ['#']
        return list1
    def deorder(self, list1):
        if list1 == []:
            return 
        elif list1[0] != '#':
            node = TreeNode(list1[0])
            list1.pop(0)
            node.left = self.deorder(list1)
            node.right = self.deorder(list1)
        else:
            list1.pop(0)
            return
        return node

        

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node1.left = node2
node1.right = node3
node2.left = node4
node3.left = node5
node3.right = node6

s = solution()
list1 = [1, 2, 4, '#', '#', '#', 3, 5, '#', '#', 6, '#', '#']

a = s.deorder(list1)
print(a.val)