'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''

class Solution:
    # 从左右一起查找
    # 因为当两个数的和一定的时候, 两个数字的间隔越大, 乘积越小
    # 所以直接输出查找到的第一对数即可
    def FindNumbersWithSum(self, array, tsum):
        if array == None or len(array) <= 0 or array[-1] + array[-2] < tsum:
            return []
        start = 0
        end = len(array)-1
        while start < end:
            sum = array[start] + array[end]

            if sum < tsum:
                start += 1
            elif sum > tsum:
                end -= 1
            else:
                return [array[start], array[end]]
        return []

'''
找出所有和为S的连续正数序列
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum + 1) // 2
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(list(range(small, big+1)))
            while curSum > tsum and small < middle:
                curSum -= small
                small += 1
                if curSum == tsum:
                    output.append(list(range(small, big+1)))
            big += 1
            curSum += big
        return output

    def FindContinuousSequence2(self, tsum):
        if tsum < 3:
            return []
        small, big = 1, 2
        middle = (tsum + 1) >> 1
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(list(range(small, big + 1)))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output
