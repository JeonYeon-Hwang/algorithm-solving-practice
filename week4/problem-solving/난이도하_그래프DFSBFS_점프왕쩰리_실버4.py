# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
import sys
from collections import deque

try:
    sys.stdin = open('난이도하_그래프DFSBFS_점프왕쩰리_실버4.txt', 'r')
except FileNotFoundError:
    pass


N = int(input().rstrip())

input = sys.stdin.readline
area = []
# visited = []
q = deque()

for _ in range(N):
    nums = input().rstrip().split(' ') 
    temp = list(map(int, nums))
    area.append(temp)
    # visited.append([False for _ in range(len(temp))])

pos = [0, 0]
dir = [[1, 0], [0, 1]]
can_arrive = False
q.append(pos)
# visited[0][0] = True


while q:
    curr_y, curr_x = q.popleft()
    move_range = area[curr_y][curr_x]
    if move_range == 0:
        break

    if move_range == -1:
        print('HaruHaru')
        can_arrive = True
        break

    for dy, dx in dir:
        new_y = curr_y + (dy * move_range)
        new_x = curr_x + (dx * move_range)

        if new_y >= len(area) or new_x >= len(area):
            continue

        q.append([new_y, new_x])
        # visited[new_y][new_x] = True


if can_arrive is False: print('Hing')
