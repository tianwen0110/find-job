"""
给一段长度长度为ｎ的绳子，把绳子减为ｍ段（ｍ，ｎ都是整数且大于１），求每段绳子乘积的最大值
"""

class solution(object):
    def cut(self, rope):
        if type(rope) != int:
            return None
        if rope < 2:
            return None
        
        maxnumber = [0 for i in range(rope+1)]
        maxnumber[1] = 1
        maxnumber[2] = 2
        maxnumber[3] = 3

        for i in range(4, rope+1):
            maxnumber[i] = maxnumber[i - 1]
            for j in range(1,i):
                if maxnumber[j] * maxnumber[i-j] > maxnumber[i]:
                    maxnumber[i] = maxnumber[j] * maxnumber[i-j]
        return maxnumber[rope]


s = solution()
print(s.cut(8))
