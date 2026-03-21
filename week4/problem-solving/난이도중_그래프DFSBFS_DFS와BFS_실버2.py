# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
import sys
from collections import deque

try:
    sys.stdin = open('난이도중_그래프DFSBFS_DFS와BFS_실버2.txt', 'r')
except FileNotFoundError:
    pass

sys.setrecursionlimit(100000)
input = sys.stdin.readline


infos = input().rstrip().split(' ')
N, M, V = list(map(int, infos))

graph = {}
temp_list = []

for _ in range(M):
    line = input().rstrip()

    temp = list(line.split(' '))
    a = int(temp[0])
    b = int(temp[1])
    
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)



# BFS의 경우 pQ를 사용, 각 뎁스마다 pQ로 정렬
# DFS의 경우 ... 일단 매번 정렬 하기로? => 차라리 얘도 pQ 사용하는게 나을 듯. 매번 하지만
# nono ... 그냥 매번 정렬 때리면 됨


# 요건 DFS임
dfs_visited = [False] * (N + 1)
dfs_answer = []

def dfs(node):     
    if dfs_visited[node] is True: return 
    dfs_visited[node] = True  
    dfs_answer.append(node)

    for neighbor in sorted(graph.get(node, [])):      
        dfs(neighbor)

dfs(V)

print(*dfs_answer)


# 요건 BFS임
q = deque()
q.append(V)
bfs_visited = [False] * (N + 1)
bfs_visited[V] = True
bfs_answer = []

def bfs():

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            bfs_answer.append(node)
            
            for neighbor in sorted(graph.get(node, [])):
                if bfs_visited[neighbor] is False:
                    bfs_visited[neighbor] = True
                    q.append(neighbor)

bfs()
print(*bfs_answer)