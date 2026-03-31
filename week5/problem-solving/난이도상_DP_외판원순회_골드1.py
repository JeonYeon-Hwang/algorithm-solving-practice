# DP - 외판원 순회 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/2098
import sys
from io import StringIO

file = """4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
"""

sys.stdin = StringIO(file)
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    row = list(map(int, input().split(' ')))
    arr.append(row)


print(arr)
