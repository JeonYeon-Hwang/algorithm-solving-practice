# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

import sys
import math

try:
    sys.stdin = open('난이도중_정수론_골드바흐의추측_실버2.txt', 'r')
except FileNotFoundError:
    pass

n = int(input())
list = []
max_num = -float('inf')
add_amout = 1

while True:
    try:
        line = int(input())
        list.append(line)
        max_num = max(line, max_num)
    except EOFError:
        break
    
#에라토스테네스의 체
is_prime = [True] * (max_num + 1)
is_prime[0] = False
is_prime[1] = False

for start in range(2, max_num + 1):
    for num in range(start, max_num + 1, start):
        if num > start:
            is_prime[num] = False

def find_prime(num):
    half = int(num / 2)
    if is_prime[half]:
        print(f"{half} {half}")
    else:
        for i in range(half + 1):
            if is_prime[half - i] and is_prime[half + i]:
                print(f"{half - i} {half + i}")
                break

for num in list:
    find_prime(num)

