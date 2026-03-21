# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724
import sys

try:
    sys.stdin = open('난이도중_그래프DFSBFS_연결요소의개수_실버2.txt', 'r')
except FileNotFoundError:
    pass



infos = input().rstrip().split(' ')
N, M = list(map(int, infos))
visited = [False] * (N + 1)

graph = {}
component = 0

for i in range(N):
    graph[i + 1] = []

input = sys.stdin.readline

for _ in range(M):
    nodes = input().rstrip().split(' ')
    nodes = list(map(int, nodes))
    
    graph[nodes[0]].append(nodes[1])
    graph[nodes[1]].append(nodes[0])


def dfs(node):
    for neighbor in graph[node]:
        if visited[neighbor] is False:
            visited[neighbor] = True
            dfs(neighbor)



for i in range(N):
    root = i + 1
    if visited[root] is False:
        component += 1
        dfs(root)

print(component)