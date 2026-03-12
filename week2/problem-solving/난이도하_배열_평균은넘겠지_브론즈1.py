# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

import sys


try:
    sys.stdin = open('난이도하_배열_평균은넘겠지_브론즈1.txt', 'r')
except FileNotFoundError:
    pass

rows = int(input())

for _ in range(rows):
    while True:
        try:
            nums = list(map(int, input().split()))
            n = len(nums) - 1
            sum = 0          
            for i in range(1, n+1):
                sum += nums[i]
            
            avg = sum/n
            above_avg_num = 0
            for i in range(1, n+1):
                if nums[i] > avg:
                    above_avg_num +=1

            answer = above_avg_num/n*100
            print(f"{answer:.3f}%")     

        except EOFError:
            break