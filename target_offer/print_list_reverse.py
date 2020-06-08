class listnode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

class solution(object):
    def reverse_list(self, first):
        if first.val == None:
            return -1
        elif first.next == None:
            return first.val
        nextnode = first
        l = []
        while nextnode != None:
            l.insert(0, nextnode.val)
            nextnode = nextnode.next
        return l

node1 = listnode(10)
node2 = listnode(11)
node3 = listnode(13)
node1.next = node2
node2.next = node3

singleNode = listnode(12)

test = listnode()

S = solution()
print(S.reverse_list(node1))