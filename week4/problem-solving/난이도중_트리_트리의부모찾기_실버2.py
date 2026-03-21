# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
import sys

try:
    sys.stdin = open('난이도중_트리_트리의부모찾기_실버2.txt', 'r')
except FileNotFoundError:
    pass

sys.setrecursionlimit(100000)
N = int(input().rstrip())
input = sys.stdin.readline
graph = {}
parents = [0] * (N + 1)
visited = [False] * (N + 1)

for i in range(N - 1):
    temp = list(input().rstrip().split(' '))
    a = int(temp[0])
    b = int(temp[1])
    
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)


def dfs(node):
    visited[node] = True

    for neighbor in graph[node]:
        if visited[neighbor] is False:
            parents[neighbor] = node
            dfs(neighbor)

dfs(1)

for i in range(2, N + 1):
    print(parents[i])