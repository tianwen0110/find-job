
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

class solution(object):
    def printM(self, matrix):
        list1 = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        if len(matrix) == 1:
            for i in range(len(matrix[0])):
                list1.append(matrix[0][i])
        elif len(matrix[0]) == 1:
            for i in range(len(matrix)):
                list1.append(matrix[i][0])
        else:
            for i in range(len(matrix[0])):
                list1.append(matrix[0][i])
            for j in range(1,len(matrix)):
                list1.append(matrix[j][i])
            for i in range(len(matrix[0])-2, -1, -1):
                list1.append(matrix[j][i])
            if len(matrix) >1:
                for j in range(len(matrix)-2, 0, -1):
                    list1.append(matrix[j][0])
        matrix1 = [[matrix[i][j] for j in range(1,len(matrix[0])-1)] for i in range(1,len(matrix)-1)]
        list1 = list1 + self.printM(matrix1)
        return list1

a = [[ 1],
 [ 5],
 [ 9],
 [13]]

s = solution()
print(s.printM(a))