# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
import sys

try:
    sys.stdin = open('난이도하_그래프DFSBFS_바이러스_실버3.txt', 'r')
except FileNotFoundError:
    pass


N = int(input().rstrip())
networks = int(input().rstrip())
graph = {}
visited = [False] * N

input = sys.stdin.readline

for i in range(N):
    graph[i + 1] = []

for _ in range(networks):
    network = list(input().rstrip().split(' '))
    a = int(network[0])
    b = int(network[1])

    graph[a].append(b)
    graph[b].append(a)



def dfs(node):
    global count
    visited[node - 1] = True
    count += 1

    for neighbor in graph[node]:
        if visited[neighbor - 1] is False:
            dfs(neighbor)


max_scope = 0
for idx in range(N):
    if visited[idx] is False:
        count = 0
        dfs(idx + 1)
        max_scope = max(max_scope, count - 1)

print(max_scope)