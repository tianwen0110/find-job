'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

class solution(object):
    def minnumber(self, array):
        if array == []:
            return None
        if type(array) != list:
            return None

        a1 = 0
        a2 = len(array)-1
        if array[a1] < array[a2]:
            return array[a1]
        while (a1 == a2 or a2 - a1==1)==False:
            a3 = int(0.5*(a1+a2))
            if array[a3] >= array[a1]:
                a1 = a3
            else:
                a2 = a3
        if array[a1]>array[a2]:
            return array[a2]
        else:
            return array[a1]
Test = solution()
print(Test.minnumber([3, 4, 5, 1, 2]))
print(Test.minnumber([1, 2, 3, 4, 5]))
print(Test.minnumber([1, 1, 1, 0, 1]))
print(Test.minnumber([1, 0, 1, 1, 1]))