# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys
from io import StringIO

file = """3
2
1 2
1000
3
1 5 10
100
2
5 7
22"""


sys.stdin = StringIO(file)

input = sys.stdin.readline
T = int(input())

# dp에 대한 감을 잡았으나, 중복 처리를 하는 것이 문제...


for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split(' ')))
    M = int(input())

    print(f'{N}, {lst}, {M}')



