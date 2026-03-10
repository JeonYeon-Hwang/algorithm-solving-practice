# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

import sys
import math


try:
    sys.stdin = open('난이도중_백트래킹_NQueen_골드4.txt', 'r')
except FileNotFoundError:
    pass

N = int(input())

# 각 선에 얼만큼 가중치가 있는지 저장하는 배열
list_y = [0] * N
list_x = [0] * N
list_cross_up = [0] * (N * 2 - 1)
list_cross_down = [0] * (N * 2 - 1)

adjust = N - 1
count = 0

def dispos_queen(temp):
    global count

    if len(temp) == N:
        count += 1
        return
    
    curr_x = len(temp)
    for curr_y in range(N):
        # 공격 가능한지 검증
        if list_y[curr_y] != 0 or \
            list_x[curr_x] != 0 or \
            list_cross_up[curr_x + curr_y] != 0 or \
            list_cross_down[adjust + (curr_y - curr_x)] != 0:
            continue
        
        # 공격 채워진 선 추가
        list_y[curr_y] += 1
        list_x[curr_x] += 1
        list_cross_up[curr_x + curr_y] += 1
        list_cross_down[adjust + (curr_y - curr_x)] += 1

        temp.append(curr_y)
        dispos_queen(temp)
        temp.pop()

        # 공격 채워진 선 제거
        list_y[curr_y] -= 1
        list_x[curr_x] -= 1
        list_cross_up[curr_x + curr_y] -= 1
        list_cross_down[adjust + (curr_y - curr_x)] -= 1

dispos_queen([])
print(count)
