# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

import sys
import math


try:
    sys.stdin = open('난이도중_완전탐색_차이를최대로_실버2.txt', 'r')
except FileNotFoundError:
    pass

n = int(input())
nums = list(map(int, input().split()))
visited = [False] * n
temp_list = []
max_sum = -sys.maxsize

def getSum(list):
    sum = 0
    for i in range(1, len(list)):
        sum += abs(list[i - 1] - list[i])
    return sum

def recursive():
    global max_sum

    if len(temp_list) == len(nums):
        sum = getSum(temp_list)
        max_sum = max(max_sum, sum)
        return

    for i in range(len(nums)):
        if visited[i]:
            continue

        num = nums[i]
        temp_list.append(num)
        visited[i] = True
        recursive()
        temp_list.pop()
        visited[i] = False

recursive()
print(max_sum)