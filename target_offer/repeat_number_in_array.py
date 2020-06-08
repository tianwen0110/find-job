'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
'''

class solution(object):
    # 输出数组中任意一个重复的数字
    def aaa(self, number):
        if len(number) == None or len(number) < 1:
            return -1
        for i in number:
            if i < 0 or i >= len(number):
                return -1
        for i in range(len(number)):
            while i != number[i]:
                if number[i] == number[number[i]]:
                    return number[i]
                else:
                    index = number[i]
                    number[i], number[index] = number[index], number[i]
        return -1
    # 输出所有重复的数字
    def bbb(self, number):
        if len(number) == None or len(number) < 1:
            return -1
        for i in number:
            if i < 0 or i >= len(number):
                return -1
        repeat_number = []
        for i in range(len(number)):
            while i != number[i]:
                if number[i] == number[number[i]]:
                    repeat_number.append(number[i])
                    break
                else:
                    index = number[i]
                    number[i], number[index] = number[index], number[i]
        if len(repeat_number) == 0:
            return -1 
        else:
            return set(repeat_number)


test = [0,1,1,2,2,3]
S = solution()

print(S.bbb(test))





        