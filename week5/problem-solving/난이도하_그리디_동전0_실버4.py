# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047
import sys
from io import StringIO

file = """10 4200
1
5
10
50
100
500
1000
5000
10000
50000"""


sys.stdin = StringIO(file)

input = sys.stdin.readline
N, K = map(int, input().rstrip().split())

coin_lst = [0] * N
total_coins = 0

for i in range(N):
    amt = int(input().rstrip())
    coin_lst[N - (i + 1)] = amt


for i in range(len(coin_lst)):
    while K >= coin_lst[i]:
        K -= coin_lst[i]      
        total_coins += 1

    if K == 0:
        break

print(total_coins)
    
