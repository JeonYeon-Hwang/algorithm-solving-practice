# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253
import sys
from io import StringIO

file = """19 3
11
6
16
"""

sys.stdin = StringIO(file)
input = sys.stdin.readline

N, M = map(int, input().split(' '))
path_bool = [True] * (N + 1) 
path_dp = [{} for _ in range(N + 1)]


for _ in range(M):
    cant_stone = int(input())
    path_bool[cant_stone] = False


if path_bool[2] is True:
    path_dp[2][1] = 1


for i in range(2, N + 1):
    for range, steps in path_dp[i].items():

        shrink = range - 1
        parallel = range
        expend = range + 1
        
        if shrink > 0 and i + shrink <= N and path_bool[i + shrink] is True:
            cur_val = path_dp[i + shrink].get(shrink, float('inf'))
            if steps + 1 < cur_val:
                path_dp[i + shrink][shrink] = steps + 1
        
        if i + parallel <= N and path_bool[i + parallel] is True: 
            cur_val = path_dp[i + parallel].get(parallel, float('inf'))
            if steps + 1 < cur_val:
                path_dp[i + parallel][parallel] = steps + 1
        
        if i + expend <= N and path_bool[i + expend] is True:
            cur_val = path_dp[i + expend].get(expend, float('inf'))
            if steps + 1 < cur_val:
                path_dp[i + expend][expend] = steps + 1
        


if len(path_dp[N]) == 0:
    print(-1)
else:
    min_case = float('inf')
    for range, steps in path_dp[N].items():
        min_case = min(min_case, steps)
    print(min_case)
