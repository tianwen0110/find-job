class treenode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class solution(object):
    def reconstructtree(self, pre, tin):
        if set(pre) != set(tin):
            return -1
        node = treenode(pre[0])
        index = tin.index(pre[0])
        if len(pre)==1:
            return node
        if index == 0:
            node.right =  self.reconstructtree(pre[index+1:], tin[index+1:])
        elif index == len(pre) - 1:
            node.left = self.reconstructtree(pre[1:index+1], tin[:index])
        else:
            node.left = self.reconstructtree(pre[1:index+1], tin[:index])
            node.right = self.reconstructtree(pre[index+1:], tin[index+1:])
        return node

pre = [1, 2, 4, 7, 3, 5, 6, 8]
tin = [4,7,2,1,5,3,8,6]
test = solution()
tree = test.reconstructtree(pre, tin)
print(tree.value)

