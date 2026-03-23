# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707
import sys

try:
    sys.stdin = open('난이도중_DFS_이분그래프_골드4.txt', 'r')
except FileNotFoundError:
    pass


input = sys.stdin.readline

# 여기서 배운 핵심: 홀수 사이클의 경우 이분 그래프가 아님
# edge 기반 탐색으로 작동, pivot이 이동할 경우 => pivot 기준 인접노드 재 순찰


def dfs(graph, colors, root):
    stack = []
    stack.append(root)
    
    while stack:
        curr = stack.pop()
        next_color = colors[curr] % 2 + 1

        for neighbor in graph[curr]:
            if colors[neighbor] == 0:
                colors[neighbor] = next_color
                stack.append(neighbor)

            elif colors[neighbor] != next_color:
                return False

    return True


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    graph = {}
    for i in range(V):
        graph[i + 1] = []

    for _ in range(E):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)
    
    colors = [0 for _ in range(V + 1)]    
    for i in range(1, V + 1):
        if colors[i] == 0:   
            if not dfs(graph, colors, i):
                print('NO')
                break
    else:
        print('YES')
    
