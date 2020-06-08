'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution(object):
    def find(self, array, target):
        if type(target) != int and type(target) != float:
            return False
        elif array == []:
            return False
        elif type(array[0][0]) != int and type(array[0][0]) != float:
            return False
        m = len(array)
        n = len(array[0])
        if target < array[0][0] or target > array[m-1][n-1]:
            return False
        i = 0
        j = n - 1
        while i < n and j >= 0:
            if array[i][j] < target:
                i = i + 1
            elif array[i][j] == target:
                return True
            else:
                j = j - 1
        return False


array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
array2 = []
array3 = [['a', 'b', 'c'],
          ['b', 'c', 'd']]
array4 = [[62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],[63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],[64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],[66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],[67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85]]


findtarget = Solution()
print(findtarget.find(array4, 10))

