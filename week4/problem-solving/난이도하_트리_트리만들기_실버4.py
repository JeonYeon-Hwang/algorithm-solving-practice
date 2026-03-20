# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
import sys

try:
    sys.stdin = open('난이도하_트리_트리만들기_실버4.txt', 'r')
except FileNotFoundError:
    pass

input = sys.stdin.readline
n, m = map(int, input().rstrip().split(' '))
lst = [ 1 for _ in range(n)]

lst[-m] = m
for i in range(n - (m + 1), 0 , -1):
    lst[i] = 2

print('0 1')
for i in range(1, len(lst)):
    how_many = lst[i]

    move_left = i
    while how_many > 1:
        how_many -= 1
        move_left += 1
        print(f'{i} {move_left}')
