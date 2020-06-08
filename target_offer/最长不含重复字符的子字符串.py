class solution(object):
    def maxlen(self, string):
        if type(string) != str:
            return None
        n = len(string)
        a = string[0]
        maxstr = string[0]
        for i in range(1,n):
            if set(a+string[i]) != set(a):
                a = a + string[i]
                if len(a) > len(maxstr):
                    maxstr = a
            else:
                j = a.find(string[i])
                a = a[j+1:] + string[i]
                if len(a) > len(maxstr):
                    maxstr = a
        return maxstr, len(maxstr)

s = solution()
maxstr, n = s.maxlen('arabcacfr')
print(maxstr, n )