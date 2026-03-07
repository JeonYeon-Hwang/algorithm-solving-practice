# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

import sys


try:
    sys.stdin = open('난이도하_문자열_문자열반복_브론즈2.txt', 'r')
except FileNotFoundError:
    pass

cases = int(input())

for _ in range(cases):
    case = input()
    repeats = case[0]
    str = ''
    for i in range(2, len(case)):
        str += case[i] * int(repeats)

    print(str)