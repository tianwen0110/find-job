
'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def findpath(self, tree, Sum):
        if tree == None:
            return None
        if Sum < tree.val:
            return False
        list1 = []
        self.findpath1(tree, Sum, list1)
    
    def findpath1(self, tree, Sum, list1):
        if Sum < tree.val:
            return None
        if Sum == tree.val:
            if tree.left == None and tree.right == None:
                list1.append(tree.val)
                print(list1)
            else:
                return None
        else:
            list2 = copy.deepcopy(list1)
            list2.append(tree.val)
            if tree.left != None:
                self.findpath1(tree.left, Sum-tree.val, list2)
            if tree.right != None:
                self.findpath1(tree.right, Sum-tree.val, list2)

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, sum):
        if not root:
            return []
        if root.left == None and root.right == None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        stack = []
        leftStack = self.pathSum(root.left, sum - root.val)
        for i in leftStack:
            i.insert(0, root.val)
            stack.append(i)
        rightStack = self.pathSum(root.right, sum - root.val)
        for i in rightStack:
            i.insert(0, root.val)
            stack.append(i)
        return stack

    # 优化写法
    def pathSum(self, root, sum):
        if not root: return []
        if root.left == None and root.right == None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        a = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in a]


pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5

s = solution()
s.findpath(pNode1, 22)