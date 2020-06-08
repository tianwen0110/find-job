class solution(object):
    def value(self, array):
        if type(array) != list:
            return None
        a = len(array)
        b = len(array[0])
        array1 = [[0 for i in range(a)] for j in range(b)]
        for i in range(a-1,-1,-1):
            for j in range(b-1,-1,-1):
                if i == a-1 and j == b-1:
                    array1[i][j] = array[i][j]
                elif i == a-1:
                    array1[i][j] = array[i][j] + array1[i][j+1]
                elif j == b-1:
                    array1[i][j] = array[i][j] + array[i+1][j]
                else:
                    if array1[i][j+1] > array1[i+1][j]:
                        array1[i][j] = array1[i][j+1] + array[i][j]
                    else:
                        array1[i][j] = array1[i+1][j] + array[i][j]
        return array1[0][0]

array = [[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]
s = solution()
print(s.value(array))





