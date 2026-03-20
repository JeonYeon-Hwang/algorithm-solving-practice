# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372
import sys

try:
    sys.stdin = open('난이도하_트리_상근이의여행_실버4.txt', 'r')
except FileNotFoundError:
    pass


T = int(input().rstrip())


input = sys.stdin.readline

case_idx = 0

while True: 
    nums = input().rstrip() 
    
    if nums == "":
        break
    temp = list(map(int, nums.split(' ')))
    
    if case_idx == 0:
        print(temp[0] - 1)
        case_idx = temp[1]
    else:
        case_idx -= 1
