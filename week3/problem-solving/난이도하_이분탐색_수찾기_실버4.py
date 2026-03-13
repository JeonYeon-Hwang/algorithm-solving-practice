# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
import sys


try:
    sys.stdin = open('난이도하_이분탐색_수찾기_실버4.txt', 'r')
except FileNotFoundError:
    pass

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

def find_num(target):
    left = 0
    right = len(N_list) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if N_list[mid] == target:
            return True
        elif target > N_list[mid]:
            left = mid + 1
        elif target < N_list[mid]:
            right = mid - 1      
    
    return False

for m in M_list:
    if find_num(m):
        print(1)
    else:
        print(0)
