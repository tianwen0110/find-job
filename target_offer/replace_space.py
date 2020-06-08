'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

class solution(object):
    def replace(self, string):
        if type(string) != str:
            return -1
        elif len(string)==0:
            return -1
        string1 = []
        for i in string:
            if i == " ":
                string1.append("%20")
            else:
                string1.append(i)
        string1 = "".join(string1)
        return string1
    def replaceSpace2(self, s):
        if type(s) != str:
            return -1
        return s.replace(' ', '%20')

s = 'we are happy'
test = solution()
print(test.replace(s))
