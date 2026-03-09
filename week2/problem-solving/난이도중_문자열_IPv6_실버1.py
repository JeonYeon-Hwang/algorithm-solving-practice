# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

import sys


try:
    sys.stdin = open('난이도중_문자열_IPv6_실버1.txt', 'r')
except FileNotFoundError:
    pass

strings = list(input().split(':'))

if strings[0] == '': 
    strings = strings[1:]
if strings[-1] == '': 
    strings = strings[:-1]
n = len(strings)

before = 0
after = 0
isCounted = False
for i in range(n):
    if strings[i] == '':
        isCounted = True
        continue
    
    strings[i] = str(strings[i]).zfill(4)
    if not isCounted:
        before += 1
    else:
        after += 1

answer = ''
repeats = 8 - (before + after)
for i in range(n):
    if i == before:
        answer += "0000:" * repeats
        continue
    answer += f"{strings[i]}:"
# print(f"{before} - {after}")
# print(strings)
print(answer[:-1])