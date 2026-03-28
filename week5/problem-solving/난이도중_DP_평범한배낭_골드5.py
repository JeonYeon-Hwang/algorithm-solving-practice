# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
import sys
from io import StringIO

file = """4 7
6 13
4 8
3 6
5 12
"""

sys.stdin = StringIO(file)
input = sys.stdin.readline

N, K = map(int, input().split(' '))
bag_infos = []

for _ in range(N):
    W, V = map(int, input().split(' '))
    bag_infos.append([W, V])


# 조합... 문제일 수 있으나, 모든 조합 경우의 수를 구하면 터짐
# 방향성 찾음. 현재 무게(idx)에서 가장 큰 무게 + 2차원 배열(해당 idx에서 사용한 배낭) 을 기반으로 구하면 됨
# => 수정: 2차원 배열 하나로 정보 저장 가능(현재로서 최댓값, 사용된 bag 정보) 
# => 풀이 영상 봄: 내가 생각했던 접근법이랑 매우 유사하다고 느끼나 상당히 간략하게 줄임
# print(bag_infos)

dp_bags = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for row in range(1, N + 1):
    for col in range(1, K + 1):
        prev = dp_bags[row - 1][col]
        col_idx = col - bag_infos[row - 1][0]
        potential = dp_bags[row - 1][col_idx] + bag_infos[row - 1][1] if col_idx >= 0 else 0

        dp_bags[row][col] = max(prev, potential)


print(dp_bags[row][col]) 
