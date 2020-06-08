
'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''
class solution(object):
    def first(self, str1):
        if type(str1) != str:
            return None
        a = str1[0]
        b = str1[0]
        for i in range(len(str1)):
            if set(a+str1[i]) != set(a):
                a = a + str1[i]
                b = b + str1[i]
            else:
                b.replace('str[i]','')
        return b[1]


a = 'abaccdeff'
ss = solution()
print(ss.first(a))
