#대칭 차집합

import sys

a, b = list(map(int, sys.stdin.readline().split()))

# groupA=sorted(a)
# groupB=sorted(b)

aSet=set(map(int,sys.stdin.readline().split()))
bSet=set(map(int,sys.stdin.readline().split()))

print(len(a-b)+len(b-a))

