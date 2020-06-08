
'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution(object):
    def merge(self, phead1, phead2):
        if phead1 == None and phead2 == None:
            return None
        elif phead1 == None:
            return phead2
        elif phead2 == None:
            return phead1
        phead = None
        if phead1.val >= phead2.val:
            phead = phead2
            phead.next = self.merge(phead1, phead2.next)
        else:
            phead = phead1
            phead.next = self.merge(phead1.next, phead2)
        return phead

node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

s = solution()
s.merge(node1, node4)
print(node3.next.val)
