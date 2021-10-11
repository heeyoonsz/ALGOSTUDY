# 콘서트

from queue import PriorityQueue
import sys

num = int(sys.stdin.readline())
tickets = list(map(int, sys.stdin.readline().split()))

tickets.sort()
count = 1

for i in tickets:
    if (i == count):
        break;
    else:
        print(count)

print(tickets[-1] + 1)
