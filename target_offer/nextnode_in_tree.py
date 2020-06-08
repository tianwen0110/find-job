
'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

class treenode(object):
    def __init__(self, value, left=None, right=None, Next=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = Next

class solution(object):
    def getnext(self, node):
        if node == None:
            return None
        
        if node.right == None:
            nextnode = node.next
            nodevalue = node
            while nextnode.right == nodevalue:
                nodevalue = nextnode
                nextnode = nextnode.next
            return nextnode
        else:
            nextnode = node.right
            nodevalue = node
            while nextnode.left != None:
                nextnode = nextnode.left
            return nextnode