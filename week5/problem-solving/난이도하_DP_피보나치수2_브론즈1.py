# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748
import sys
from io import StringIO

file = """17"""


sys.stdin = StringIO(file)

input = sys.stdin.readline
n = int(input().rstrip())

if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n >= 2:
    fibo = [0] * (n + 1)
    fibo[1] = 1

    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    print(fibo[n])