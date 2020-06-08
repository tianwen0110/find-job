'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如 [[a b c e], [s f c s], [a d e e]] 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''
class solution(object):
    def has_path(self, matrix, path):
        raw = len(matrix)
        col = len(matrix[0])
        visit = [[0 for i in range(col)] for j in range(raw)]
        if raw == 0 or col == 0:
            return None
        for i in range(raw):
            for j in range(col):
                if self.has_path_core(matrix, i, j, raw, col, visit, path):
                    return True
        return False

    def has_path_core(self, matrix, i, j, raw, col, visit, path):
        if len(path) == 0:
            return True
        if i<0 or i>=raw or j<0 or j>=col:
            return False
        if matrix[i][j] != path[0]:
            return False
        elif visit[i][j] == 1:
            return False
        else:
            visit1 = visit
            visit1[i][j] = 1
            path1 = path[1:]
        if self.has_path_core(matrix, i+1, j, raw, col, visit1, path1) or \
            self.has_path_core(matrix, i-1, j, raw, col, visit1, path1) or \
                self.has_path_core(matrix, i, j+1, raw, col, visit1, path1) or \
                    self.has_path_core(matrix, i, j-1, raw, col, visit1, path1):
                    return True
        else:
            visit[i][j] = 0
            return False

a = [['a','b','t','g'],['c','f','c','s'],['j','d','e','h']]
b = ['b','f','c','e']
s = solution()
print(s.has_path(a,b))