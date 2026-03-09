# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

import sys
import math


try:
    sys.stdin = open('난이도중_백트래킹_NQueen_골드4.txt', 'r')
except FileNotFoundError:
    pass

N = int(input())

chosen = set()
list = [set() for _ in range(N)]
count = 0

def recursion_back(temp):
    global count

    if len(temp) == N:
        print(f"최종: {temp}")
        count += 1
        return

    compare_set = list[len(temp)]
    # print(f"{list} - {temp}")
    # print(f"비교군: {compare_set} - {chosen}")
    for i in range(N):
        # print(f"현재 순회 변수-- {i}")
        if i in compare_set:
            # print(f"compare_set에 있음: {i}")
            continue
        if i in chosen:
            # print(f"chosen에 있음: {i}")
            continue

        setting_set(i, temp)
        temp.append(i)
        # print(f"넣는 변수: {i}")
        # print(f"전반적 지도: {list}")
        # print(f"-----------")
        recursion_back(temp)
        removing_set(i, temp)
        temp.pop()


def setting_set(i, temp):
    x_pos = len(temp)
    # print(f"x_pos {x_pos}")
    chosen.add(i)
    #아래 대각선
    for o in range(i, N): 
        y_pos = x_pos + (o - i)  
        # print(f"y_pos {y_pos}") 
        if o >= N or o < 0 or y_pos >= N or y_pos < 0:
            continue
        list[y_pos].add(o)

    # 위 대각선
    for o in range(i, -1, -1): # 2 1 0 순
        # print(f"o: {o} o - i: {o - i}")
        y_pos = x_pos - (o - i)   
        # print(f"y_pos {y_pos}")
        if o >= N or o < 0 or y_pos >= N or y_pos < 0:
            continue
        list[y_pos].add(o)    

def removing_set(i, temp):
    x_pos = len(temp) - 1
    # print(f"x_pos {x_pos}")
    chosen.discard(i)
    for o in range(i, N):   # 반대로 지우면 됨
        y_pos = x_pos + (o - i)   
        if o >= N or o < 0 or y_pos >= N or y_pos < 0:
            continue
        # print(o)
        list[y_pos].discard(o)

    #위 대각선
    for o in range(i, -1, -1): # 2 1 0 순
        # print(f"o: {o} o - i: {o - i}")
        y_pos = x_pos - (o - i)   
        # print(f"y_pos {y_pos}")
        if o >= N or o < 0 or y_pos >= N or y_pos < 0:
            continue
        list[y_pos].discard(o)  

recursion_back([])
print(count)

# setting_set(2, [1])
# removing_set(2, [1, 1])
# print(f"들어감: {list}")