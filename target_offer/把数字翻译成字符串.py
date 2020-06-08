class solution(object):
    def trans(self, number):
        if type(number) != int:
            return None
        if number < 0:
            return None
        num = str(number)
        length = len(num)
        a = [0 for i in range(length+1)]
        for i in range(length, 0, -1):
            if i == length :
                a[i] = 1
            elif i == length-1:
                if int(num[-2:])<26:
                    a[i] = 2
                else:
                    a[i] = 1
            else:
                if int(num[i-1:i+1])<26:
                    a[i] = a[i+1]+a[i+2]
                else:
                    a[i] = a[i+1]
        return a[1]

num = -122
s = solution()
print(s.trans(num))
