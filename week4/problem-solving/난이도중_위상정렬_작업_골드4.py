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

for i in range(N):
    graph[i + 1] = []


for i in range(N):
    infos = input().rstrip().split(' ')
    infos = list(map(int, infos))
    print(infos)
    if infos[1] == 0: continue
    
    parents = infos[2:]
    for node in parents:
        graph[node].append(i + 1)
        in_degreee[i + 1] += 1

print(graph)
print(in_degreee)