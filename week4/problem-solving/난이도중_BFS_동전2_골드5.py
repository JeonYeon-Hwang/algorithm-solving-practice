# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294
import sys

try:
    sys.stdin = open('난이도중_BFS_동전2_골드5.txt', 'r')
except FileNotFoundError:
    pass


input = sys.stdin.readline

INF = 10001 
n, k = map(int, input().split())
coin_vals = []
dp = [INF] * (k + 1)
dp[0] = 0

for _ in range(n):
    val = int(input())
      
    if val <= k:
        coin_vals.append(val)

# python으로 BFS 방식으로 풀면 터진다는 말을 듣고 dp로 풀려고 합니다

for cur_val in range(1, k + 1):
    for val in coin_vals:
        if cur_val - val >= 0:
            amount = dp[cur_val - val] + 1
            dp[cur_val] = min(amount, dp[cur_val])


print(dp[k] if dp[k] != INF else -1)
            
