
'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

'''
相当于按层遍历, 中间需要队列做转存
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def printF(self, tree):
        if tree == None:
            return None
        list1 = []
        list1.append(tree)
        list2 = []
        while list1 != []:
            list2.append(list1[0].val)
            if list1[0].left != None:
                list1.append(list1[0].left)
            if list1[0].right != None:
                list1.append(list1[0].right)
            list1.pop(0)
        print(list2)

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
s.printF(pNode1)