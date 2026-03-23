# 그래프, DFS, BFS - 아침 산책 (백준 골드3)
# 문제 링크: https://www.acmicpc.net/problem/21606
import sys
from collections import deque

try:
    sys.stdin = open('난이도상_그래프DFSBFS_아침산책_골드3.txt', 'r')
except FileNotFoundError:
    pass


input = sys.stdin.readline

N = int(input())
nodes = [int(i) for i in list(input().rstrip())]
visited = [False] * (N + 1)
graph = {}
sum = 0


for _ in range(N - 1):
    u, v = map(int, input().split())

    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

# 규칙을 찾기 모호해서 bfs안에 bfs를 하는 방법으로 우회함
# 방향을 바꿈. 일단 bfs가 아닌 모든 노드 순회하며 실외 인접노드 찾기로
def search(nodes):
    global sum

    for node in range(1, N + 1):
        if visited[node] is False and nodes[node - 1] == 0:
            # edge_nodes => 실외에 인접한 모든 실내의 노드
            n = find_all_outside(node)
            cases = n * (n - 1)
            sum += cases
        elif visited[node] is False and nodes[node - 1] == 1:
            n = find_adjacent_inside(node)
            sum += 2 * (n - 1)


# 이걸로 인접한 모든 실외 노드를 찾습니다 => set으로 반환
# Tree 구조인 만큼, 실외 node의 수는 경우의 수에 영향을 주지 않는다
def find_all_outside(root):
    global visited

    s = set()
    s.add(root)
    q = deque()
    q.append(root)
    visited[root] = True

    edge_nodes = set()
    edge_nodes.add(root)

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if visited[next] is False and nodes[next - 1] == 0:
                visited[next] = True
                q.append(next)
                s.add(next)

    for node in s:
        for edge_node in graph[node]:
            edge_nodes.add(edge_node)

    return len(edge_nodes) - len(s)


# 이제 인접한 실내 노드들을 찾아야 함 => 경우의 수는 n - 1 개
def find_adjacent_inside(root):
    global visited 

    q = deque()
    q.append(root)
    visited[root] = True
    inside_node = 1

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if visited[next] is False and nodes[next - 1] == 1:
                visited[next] = True
                q.append(next)
                inside_node += 1

    return inside_node


search(nodes)
print(sum)