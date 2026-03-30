# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931
import sys
from io import StringIO

file = """11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""

sys.stdin = StringIO(file)
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    start, end = map(int, input().split(' '))
    lst.append((start, end))

lst.sort(key=lambda x: (x[1], x[0]))
# print(lst)
selected = []
selected.append(lst[0])

for i in range(1, len(lst)):
    if selected[-1][1] <= lst[i][0]:
        selected.append(lst[i])

print(len(selected))