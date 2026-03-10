# 백트래킹 - 비숍 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1799

import sys
import math


try:
    sys.stdin = open('난이도상_백트래킹_비숍_플래5.txt', 'r')
except FileNotFoundError:
    pass

N = int(input())
board = []

down_cross = [0] * (2 * N - 1)
up_cross = [0] * (2 * N - 1)

adjust = N - 1
cross_n = 2 * N - 1

list_even = []
list_odd = []

max_count_even = 0
max_count_odd = 0
count = 0

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

# 일단 검은색 흰색 칸을 뽑아놓기
for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            if (y + x) % 2 == 0:
                list_even.append([y, x])
            elif (y + x) % 2 != 0:
                list_odd.append([y, x])

def dispose_bishop(idx, isEven):
    global count, max_count_even, max_count_odd
    
    # 검은색 흰색 칸 구별
    if isEven:
        max_count_even = max(max_count_even, count)
    elif not isEven:
        max_count_odd = max(max_count_odd, count)

    curr_list = list_even if isEven else list_odd
    if idx == len(curr_list):
        return

    for i in range(idx, len(curr_list)):
            y, x = curr_list[i]

            # 공격 가능한지 검증
            if down_cross[adjust + (y - x)] != 0 or \
                up_cross[y + x] != 0:
                continue

            # 공격 시 공격 가능 선 추가
            down_cross[adjust + (y - x)] += 1
            up_cross[y + x] += 1 
            
            count += 1
            dispose_bishop(i + 1, isEven)
            count -= 1
            # 백 트래킹, 공격 가능 선 제거
            down_cross[adjust + (y - x)] -= 1
            up_cross[y + x] -= 1


dispose_bishop(0, True)
dispose_bishop(0, False)
print(max_count_odd + max_count_even)
# print(list_odd)
# print(list_even)