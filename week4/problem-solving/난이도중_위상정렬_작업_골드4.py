# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056
import sys
from collections import deque

try:
    sys.stdin = open('난이도중_위상정렬_작업_골드4.txt', 'r')
except FileNotFoundError:
    pass

sys.setrecursionlimit(100000)

input = sys.stdin.readline
N = int(input().rstrip())

graph = {}
in_degreee = [0] * (N + 1)
times = [0] * (N + 1)
arrival_time = [0] * (N + 1)
topo_order = []


for i in range(N):
    graph[i + 1] = []

for i in range(N):
    infos = input().rstrip().split(' ')
    infos = list(map(int, infos))
    times[i + 1] = infos[0]

    if infos[1] == 0: continue
    
    parents = infos[2:]
    for node in parents:
        graph[node].append(i + 1)
        in_degreee[i + 1] += 1


zero_in_degreee = deque()


for i in range(1, N + 1): 
    if in_degreee[i] == 0: zero_in_degreee.append(i)

while zero_in_degreee:
    # curr 노드의 작업이 수행됨을 의미
    curr = zero_in_degreee.popleft()
    topo_order.append(curr)

    # 시간 구하는 작업
    taking_time = times[curr] + arrival_time[curr]

    for neighbor in graph[curr]:
        in_degreee[neighbor] -= 1
        
        # 다음 노드에서 걸리는 시간 구하기: max로
        arrival_time[neighbor] = max(arrival_time[neighbor], taking_time)
        if in_degreee[neighbor] == 0:
            zero_in_degreee.append(neighbor)

final = 0
for i in range(N + 1):
    final = max(final, times[i] + arrival_time[i])

print(final)