# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
import sys


try:
    sys.stdin = open('난이도중_이분탐색_두용액_골드5.txt', 'r')
except FileNotFoundError:
    pass

N = input()
lst = list(map(int, input().split(" ")))
lst.sort()

candidate_l = 0
candidate_r = 0
min_sum = 2000000001

for i in range(len(lst) - 1):
    fixed_val = lst[i]
    left = i + 1
    right = len(lst) - 1
    candidate_mid = right

    while left <= right:
        mid = (left + right) // 2
        mid_val = lst[mid]
        gap = fixed_val + mid_val

        if abs(gap) < min_sum:
            min_sum = abs(gap)
            candidate_l = i
            candidate_r = mid

        if gap == 0:
            candidate_mid = mid
            break
        elif gap < 0:
            left = mid + 1
        elif gap > 0:
            right = mid - 1
        
        candidate_mid = mid
    
    candidate_sum = (fixed_val + lst[candidate_mid])
    if abs(min_sum) > abs(candidate_sum):
        min_sum = abs(candidate_sum)
        candidate_l = i
        candidate_r = candidate_mid

print(f"{lst[candidate_l]} {lst[candidate_r]}")


