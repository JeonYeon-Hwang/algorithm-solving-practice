# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

import sys


try:
    sys.stdin = open('난이도하_파이썬문법_최댓값_브론즈3.txt', 'r')
except FileNotFoundError:
    pass

order = 1
max_num = 0
max_order = 1

while True:
    try:
        line = int(input())
        if(line > max_num):
            max_num = line
            max_order = order

        order += 1
    except EOFError:
        break

print(max_num)
print(max_order)