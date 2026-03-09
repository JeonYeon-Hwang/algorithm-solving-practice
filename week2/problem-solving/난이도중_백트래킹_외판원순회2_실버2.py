# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

import sys
import math


try:
    sys.stdin = open('난이도중_백트래킹_외판원순회2_실버2.txt', 'r')
except FileNotFoundError:
    pass

N = int(input())
paths = []
temp = []
visited = [False] * N
min_val = float('inf')

for _ in range(N):
    row = list(map(int, input().split()))
    paths.append(row)

def permutation(start):
    global min_val

    if start == N:
        sum, is_able = search_routes(temp)
        if is_able:
            # print(sum)
            min_val = min(min_val, sum)
        return
    
    for i in range(N):
        if visited[i]:
            continue

        temp.append(i)
        start += 1
        visited[i] = True
        permutation(start)
        temp.pop()
        start -= 1
        visited[i] = False
        

def search_routes(list):
    sum = 0
    is_able = True
    for i in range(len(list) - 1): 
        pre = list[i]
        curr = list[i + 1]

        if paths[pre][curr] == 0:
            is_able = False
            break
        else:
            sum += paths[pre][curr]
    
    # 마지막 출발지로 도착
    if paths[list[N - 1]][list[0]] == 0:
        is_able = False
    else:
        sum += paths[list[N - 1]][list[0]]

    return sum, is_able

permutation(0)
print(min_val)

