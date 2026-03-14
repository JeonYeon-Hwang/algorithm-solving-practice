# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309
import sys
from collections import deque

try:
    sys.stdin = open('난이도중_링크드리스트_철도공사_골드4.txt', 'r')
except FileNotFoundError:
    pass

input = sys.stdin.readline
N, M = map(int, input().split(" "))
station_nums = list(map(int, input().split(" ")))

nxt = [0] * 1000001
pre = [0] * 1000001
ans = []


for i in range(len(station_nums)):
    station_num = station_nums[i]
    nxt[station_num] = station_nums[(i + 1) % N]
    pre[station_num] = station_nums[(i - 1) % N]

for _ in range(M):
    construction_infos = input().split()
    order = construction_infos[0]
    num_i = int(construction_infos[1])
    
    if order == 'BN':
        j = int(construction_infos[2])
        next_station_num = nxt[num_i]
        ans.append(str(next_station_num))
        
        nxt[j] = next_station_num
        pre[j] = num_i
        nxt[num_i] = j
        pre[next_station_num] = j

    elif order == 'BP':
        j = int(construction_infos[2])
        prev_station_num = pre[num_i]
        ans.append(str(prev_station_num))

        nxt[j] = num_i
        pre[j] = prev_station_num
        pre[num_i] = j
        nxt[prev_station_num] = j

    elif order == 'CP':
        target_to_close = pre[num_i]
        ans.append(str(target_to_close))

        prev_prev_station_num = pre[target_to_close]
        pre[num_i] = prev_prev_station_num
        nxt[prev_prev_station_num] = num_i

    elif order == 'CN':
        target_to_close = nxt[num_i]
        ans.append(str(target_to_close))

        next_next_station_num = nxt[target_to_close]
        nxt[num_i] = next_next_station_num
        pre[next_next_station_num] = num_i


sys.stdout.write('\n'.join(ans) + '\n')
