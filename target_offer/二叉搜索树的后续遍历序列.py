'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
'''

class solution(object):
    def verify(self, sequence):
        if sequence == []:
            return None
        mid = sequence[-1]
        if len(sequence) == 1:
            return True
        for i in range(len(sequence)-1):
            if sequence[i] > mid:
                break
        if i != len(sequence)-2:
            for j in range(i, len(sequence)-1):
                if sequence[j] < mid:
                    return False
            left_se = sequence[:i]
            right_se = sequence[i:-1]
        else:
            left_se = sequence[:i+1]
            right_se = []
        if left_se != []:
            left = self.verify(left_se)
        else:
            left = True
        if right_se != []:
            right = self.verify(right_se)
        else:
            right = True
        
        return left and right

array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [5,4,3,2,1]
s = solution()

print(s.verify(array3))
