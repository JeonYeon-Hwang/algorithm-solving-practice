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
# => 수정: 2차원 배열 하나로 정보 저장 가능(현재로서 최댓값, 사용된 bag 정보) => 풀이 영상 봄: 내가 생각했던 접근법이랑 매우 유사함

# print(bag_infos)

dp_bags = [[0 for _ in range(N)] for _ in range(K + 1)]

for i in range(1, K + 1):

    # 일단 이전 값으로 갱신 진행
    for j in range(N):
        dp_bags[i][j] = dp_bags[i - 1][j] 

    for j in range(N):
        weight, val = bag_infos[j]
        

        if i - weight >= 0:
            prev_max = 0

            # for n in range(N):
