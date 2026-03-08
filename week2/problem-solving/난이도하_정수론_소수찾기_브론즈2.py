# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

import sys
import math

try:
    sys.stdin = open('난이도하_정수론_소수찾기_브론즈2.txt', 'r')
except FileNotFoundError:
    pass

num_of_nums = int(input())
num_of_prime = 0
data = list(map(int, input().split()))

def isPrime(num):
    if num == 1:
        return False
    elif num < 2:
        return True
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True

for num in data:
    if isPrime(num):
        num_of_prime += 1

print(num_of_prime)