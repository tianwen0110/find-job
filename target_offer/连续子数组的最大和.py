'''
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''

class solution(object):
    def findmaxnum(self, list1):
        if type(list1) != list:
            return None
        maxnum = 0
        maxnum1 = 0
        for i in list1:
            if i >= 0:
                maxnum1 = maxnum1 + i
                if maxnum1 > maxnum:
                    maxnum = maxnum1
            else:
                if maxnum1 + i >= 0:
                    maxnum1 = maxnum1 + i
                else:
                    maxnum1 = 0
        return maxnum

alist = [1, -2, 3, 10, -4, 7, 2, -5]
s = solution()
print(s.findmaxnum(alist))
