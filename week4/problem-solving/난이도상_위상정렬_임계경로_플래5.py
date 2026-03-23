# 위상정렬 - 임계경로 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1948
import sys
from collections import deque

try:
    sys.stdin = open('난이도상_위상정렬_임계경로_플래5.txt', 'r')
except FileNotFoundError:
    pass

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = {}
in_degree = [0] * (n + 1)
topo_order = []

for _ in range(m):
    u, v, m = map(int, list(input().rstrip().split()))
    graph.setdefault(u, []).append((v, m))
    in_degree[v] += 1

han, rome = map(int, input().split())
graph.setdefault(rome, [])

zero_in_degree = deque([x for x in range(1, n + 1) if in_degree[x] == 0])
arrival_infos = [[] for _ in range(n + 1)]


# 계산하면서 최대 남은 시간 업데이트 + 동일 시 병렬 처리, 동시에 이전 노드도 기록
while zero_in_degree:
    cur = zero_in_degree.popleft()
    topo_order.append(cur)

    # 현재 시간 구하기
    pre_weight = 0 if len(arrival_infos[cur]) == 0 else arrival_infos[cur][0][0]

    for next, weight in graph[cur]:
        in_degree[next] -= 1

        # 노드에 걸리는 시간 구하기
        if len(arrival_infos[next]) == 0:
            arrival_infos[next].append((weight + pre_weight, cur))
        else:
            candi_weight = arrival_infos[next][0][0]
            # 새로운 대안이 더 max 시 => 기존 튜플 모두 삭제
            if candi_weight < weight + pre_weight:
                arrival_infos[next] = []
                arrival_infos[next].append((weight + pre_weight, cur))
            # 동일한 max 발견 시 => 병렬하기
            elif candi_weight == weight + pre_weight:
                arrival_infos[next].append((weight + pre_weight, cur))

        if in_degree[next] == 0:
            zero_in_degree.append(next)


# 역추적 => 재귀 스택 많을 거 같아 bfs로
edges = 0
q = deque()
lst = arrival_infos[rome]
visited = [False] * (n + 1)

for i in range(len(lst)):
    q.append(arrival_infos[rome][i][1])

while q:
    cur = q.popleft()
    edges += 1
    if visited[cur] is True:
        continue

    visited[cur] = True   
    for weight, parent in arrival_infos[cur]:
        q.append(parent)


print(arrival_infos[rome][0][0])
print(edges)
