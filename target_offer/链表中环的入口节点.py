'''
一个链表中包含环，请找出该链表的环的入口结点。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 没有考虑自环，只需加一次判断
class solution(object):
    def meetnode(self, head):
        if head == None:
            return None
        pslow = head.next
        if pslow == None:
            return None
        pfast = pslow.next
        if pfast == None:
            return None
        while pslow != pfast:
            pslow = pslow.next
            pfast = pfast.next
            if pfast == None:
                return None
            pfast = pfast.next
            if pfast == None:
                return None
        i = 1
        pfast = pfast.next
        # 这里没有考虑自环，只需加一次判断
        while pslow != pfast:
            pfast = pfast.next
            i = i + 1
        pfast = head
        pslow = head
        for j in range(i):
            pfast = pfast.next
        i = 0
        while pfast != pslow:
            pfast = pfast.next
            pslow = pslow.next
        return pfast.val

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node1
        
s = solution()
print(s.meetnode(node1))
