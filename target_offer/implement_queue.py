
'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

class solution(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def append_element(self, x):
        self.stack1.append(x)
    def push_element(self):
        if  len(self.stack2) == 0 and len(self.stack1) == 0:
            return None
        while len(self.stack2) != 0:
            return self.stack2.pop()
        while len(self.stack1) != 0:
            a = self.stack1[-1]
            self.stack2.append(a)
            self.stack1.pop()
        return self.stack2.pop()


p = solution()
p.append_element(10)
p.append_element(15)
p.append_element(20)
print(p.push_element())
p.append_element(25)
print(p.push_element())
print(p.push_element())
print(p.push_element())
print(p.push_element())
print(p.push_element())
print(p.push_element())
