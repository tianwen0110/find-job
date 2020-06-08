'''
统计一个数字在排序数组中出现的次数。
'''

'''
二分查找的扩展。可以构造两个函数。第一个函数查找目标数字出现的最前面的位置，先使用二分查找找到该数字，
如果该数字的index > 0而且该数字前面一个数字等于k的话，那么就令end=middle-1，继续二分查找。
对于第二个函数，查找目标数字出现的最后面的位置，反之编写。最后如果数字存在的话，
令走后面的index减去最前面的index然后+1即可。在进行有序数组的元素查找，可以先尝试一下二分查找
'''

class Solution:
    def GetNumberOfK(self, data, k):
        number = 0
        if data != None and len(data) > 0:
            length = len(data)
            first = self.GetFirstK(data, length, k, 0, length-1)
            last = self.GetLastK(data, length, k, 0, length-1)
            if first > -1:
                number = last - first + 1
        return number

    def GetFirstK(self, data, length, k, start, end):
        if start > end:
            return -1

        middleIndex = (start + end) // 2
        middleData = data[middleIndex]

        if middleData == k:
            if middleIndex > 0 and data[middleIndex-1] == k:
                end = middleIndex - 1
            else:
                return middleIndex
        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1
        return self.GetFirstK(data, length, k, start, end)

    def GetLastK(self, data, length, k, start, end):
        if start > end:
            return -1

        middleIndex = (start + end) // 2
        middleData = data[middleIndex]

        if middleData == k:
            if middleIndex < end and data[middleIndex+1] == k:
                start = middleIndex + 1
            else:
                return middleIndex
        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1
        return self.GetLastK(data, length, k, start, end)