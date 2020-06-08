'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

class solution(object):
    def uglynum(self, num):
        if type(num) != int or num < 1:
            return None
        a = [1]
        a2 = 0
        a3 = 0
        a5 = 0
        if num == 1:
            return 1
        for i in range(1,num):
            aa = min(a[a2]*2, a[a3]*3,a[a5]*5)
            while aa <= a[i-1]:
                aa = min(a[a2]*2, a[a3]*3,a[a5]*5)
                if aa == a[a2]*2:
                    a2 = a2 + 1
                elif aa == a[a3]*3:
                    a3 = a3 + 1
                else:
                    a5 = a5 + 1
            a.append(aa)
        return a[num-1]

s = solution()
print(s.uglynum(7))
