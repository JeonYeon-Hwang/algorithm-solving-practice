# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178
import sys
from collections import deque

try:
    sys.stdin = open('난이도중_BFS_미로탐색_실버1.txt', 'r')
except FileNotFoundError:
    pass


input = sys.stdin.readline
N, M = map(int, input().split())
maze = []
visited = []

for _ in range(N):
    rows = [int(i) for i in input().rstrip()]
    v_rows = [False for _ in range(M)]

    maze.append(rows)
    visited.append(v_rows)


def bfs(maze):
    q = deque()
    q.append([0, 0])
    visited[0][0] = True

    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while q:
        cur = q.popleft()
        cur_y = cur[0]
        cur_x = cur[1]

        for i in range(4):
            y = cur_y + d[i][0]
            x = cur_x + d[i][1]

            if y < 0 or y >= N or x < 0 or x >= M:
                continue
            if maze[y][x] == 0:
                continue
            
            # 최적값인지 필터링 하기
            if maze[y][x] < maze[cur_y][cur_x] + 1 and maze[y][x] != 1:
                continue
            
            if visited[y][x] is True:
                continue           
            visited[y][x] = True

            # 값 업데이트
            maze[y][x] = maze[cur_y][cur_x] + 1

            q.append([y, x])


bfs(maze)
print(maze[N - 1][M - 1])