# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251
import sys
from io import StringIO

file = """ACAYKP
CAPCAK"""


sys.stdin = StringIO(file)

input = sys.stdin.readline

fst = input().rstrip()
sec = input().rstrip()

n = len(fst)
m = len(sec)

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if fst[i - 1] == sec[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[n][m])