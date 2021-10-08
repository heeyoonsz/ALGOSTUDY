# BABBA

import sys

'''
A=>B , B=>BA

0:A //a=1 b=0
1:B //a=0 b=1
2:BA // a=1 b=1
3:BAB // a=1 b=2
4:BABBA // a=2 b=3
5:BABBABAB // a=3 b=5
6:BABBABABBABBA// a=5 b=8
7:BA B BA BA B BA B BA BA B BA BA B //a=8 b=13

'''
a = [0] * 46
b = [0] * 46

num = int(sys.stdin.readline())

a[0] = 1
a[1] = 0

b[0] = 0
b[1] = 1

for i in range(2,num + 1):
    a[i] = a[i - 1] + a[i - 2]
    b[i] = b[i - 1] + b[i - 2]
print(str(a[num]) + ' ' + str(b[num]))
