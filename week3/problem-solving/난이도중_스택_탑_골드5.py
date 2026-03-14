# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493
import sys


try:
    sys.stdin = open('난이도중_스택_탑_골드5.txt', 'r')
except FileNotFoundError:
    pass

N = int(input())
lst = list(map(int, input().split(" ")))
stack = []
observe_info = [0] * len(lst)

for i in range(len(lst) - 1, -1, -1):
    curr_height = lst[i]
    curr_order = i

    if len(stack) == 0:
        stack.append([curr_height, curr_order])
        continue
    else:
        while len(stack) != 0 and curr_height >= stack[-1][0]:
            poped = stack.pop()
            poped_order = poped[1]
            observe_info[poped_order] = curr_order + 1
        
        stack.append([curr_height, curr_order])
    

result = " ".join([str(i) for i in observe_info])
print(result)