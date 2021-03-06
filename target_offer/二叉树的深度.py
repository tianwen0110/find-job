'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def depth(self, treenode):
        if treenode.left == None and treenode.right == None:
            return 1
        elif treenode.left ==None:
            return self.depth(treenode.right) + 1
        elif treenode.right == None:
            return self.depth(treenode.left) + 1
        else:
            if self.depth(treenode.left) > self.depth(treenode.right):
                return self.depth(treenode.left) + 1
            else:
                return self.depth(treenode.right) + 1


