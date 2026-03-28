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
22
"""


sys.stdin = StringIO(file)

input = sys.stdin.readline
T = int(input())

# dp에 대한 감을 잡았으나, 중복 처리를 하는 것이 문제...
# 탑 다운 방식으로 접근하기로...
# 드디어 문제에 접근하게 됨 => 2차원 dp 문제임

for _ in range(T):
    N = int(input())
    amt_lst = list(map(int, input().split(' ')))
    M = int(input())

    cases_dp = [[0 for _ in range(N)] for _ in range(M + 1)]

    for i in range(N):
        gap = amt_lst[i]
        if gap <= M: 
            cases_dp[gap][i] = 1   

    for i in range(M + 1):
        for j in range(N):
            case_count = cases_dp[i][j]

            if case_count != 0:
                for n in range(j, N):
                    gap = amt_lst[n]
                    if i + gap <= M:
                        cases_dp[i + gap][n] += case_count

    sum = 0
    for i in range(N):
        sum += cases_dp[M][i]

    print(sum)



