
'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''

class solution(object):
    def match(self, string, pattern):
        if type(string)!=str or type(pattern)!=str:
            return None
        i = 0
        j = 0
        length = len(string)
        while i != length:
            if j>=len(pattern):
                return False
            if string[i]==pattern[j]:
                i = i+1
                j = j+1
            elif pattern[j]=='*':
                if string[i]==pattern[j+1]:
                    i = i+1
                    j = j+2
                elif string[i]==string[i-1]:
                    i = i+1
                else:
                    return False
            elif pattern[j] == '.':
                i = i+1
                j = j+1
            elif pattern[j+1]=='*':
                j = j+2
        if j ==len(pattern):
            return True
        else:
            return False

s = solution()
a = 'a.a'
b = 'ab*ac*a'
k = 'aaa'
c = 'aa.a'
d = 'ab*a'
print(s.match(k,d))


                


                
