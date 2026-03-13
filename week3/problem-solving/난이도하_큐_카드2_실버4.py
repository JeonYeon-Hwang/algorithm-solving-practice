# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
import sys
from collections import deque

try:
    sys.stdin = open('난이도하_큐_카드2_실버4.txt', 'r')
except FileNotFoundError:
    pass

input = sys.stdin.readline
N = int(input())

queue = deque()

for i in range(1, N + 1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    be_last = queue.popleft()
    queue.append(be_last)


print(queue[0])