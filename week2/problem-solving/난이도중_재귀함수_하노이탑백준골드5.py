# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

import sys


try:
    sys.stdin = open('난이도중_재귀함수_하노이탑백준골드5.txt', 'r')
except FileNotFoundError:
    pass

floors = int(input())

print(2 ** floors - 1)

def recursion_move(floors, start, end):
    if floors == 1:
        print(f"{start} {end}")
        return
    
    mid = 6 - start - end

    recursion_move(floors - 1, start, mid)
    print(f"{start} {end}")
    recursion_move(floors - 1, mid, end)

if floors <= 20:
    recursion_move(floors, 1, 3)

