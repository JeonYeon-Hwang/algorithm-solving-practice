# 정수론 - 제곱 ㄴㄴ 수 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1016

import sys
import math

try:
    sys.stdin = open('난이도상_정수론_제곱ㄴㄴ수_골드1.txt', 'r')
except FileNotFoundError:
    pass

list = list(map(int, input().split()))
min = list[0]
max = list[1]

max_pow = int(math.sqrt(max))
count = 0

is_squar_nums = [False] * (max - min + 1)

for i in range(2, max_pow + 1):
    square = i * i

    start_val = (min // square) * square
    if start_val < min:
        start_val += square

    for j in range(start_val, max + 1, square):
        # print(j)
        is_squar_nums[j - min] = True

for is_squar in is_squar_nums:
    if not is_squar:
        count += 1

print(count)