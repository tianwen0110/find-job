
'''
求出1~n的整数中1出现的次数？
1~13中包含1的数字有1、10、11、12、13因此共出现6次。
'''

class solution(object):
    def frequence(self, num):
        if type(num) != int or num < 1:
            return None
        num1 = num // 10
        list1 = [num%10]
        while num1 != 0:
            num = num1
            num1 = num1 //10
            list1.append(num%10)
        fre = 0
        for i in range(1,len(list1)):
            fre1 = 0
            for j in range(i, len(list1)):
                fre1 = fre1 + list1[j]*(10**(j-i))
            if list1[i-1] < 1:
                fre = fre + fre1
            elif list1[i-1] == 1:
                for j in range(i-1):
                    fre = fre + list1[j]*(10**j)
                fre = fre + 1 + fre1*10**(i-1)
            else:
                fre = fre + (fre1+1)*10**(i-1)
        if list1[i] < 1:
            fre = fre
        elif list1[i] == 1:
            for j in range(i):
                fre = fre + list1[j]*(10**j)
            fre = fre + 1 + fre1*10**(i-1)
        else:
            fre = fre + 10**i
        return fre

s = solution()
print(s.frequence(2134))


