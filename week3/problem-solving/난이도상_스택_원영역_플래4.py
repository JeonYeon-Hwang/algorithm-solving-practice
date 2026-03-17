# 스택 - 원 영역 (백준 플래4)
# 문제 링크: https://www.acmicpc.net/problem/10000
import sys

try:
    sys.stdin = open('난이도상_스택_원영역_플래4.txt', 'r')
except FileNotFoundError:
    pass

ob = sys.stdin.readline
N = int(input().rstrip())

areas = 1
stack = []
circle_infos = []

for _ in range(N):
    input = sys.stdin.readline
    x, r = list(map(int, input().rstrip().split(" ")))
    circle_infos.append([x - r, 'left', 2 * r])
    circle_infos.append([x + r, 'right', 2 * r])

circle_infos.sort(key=lambda x: (
    x[0],
    0 if x[1] == 'right' else 1,
    -x[2] if x[1] == 'left' else x[2]
    ))

for i in range(0, len(circle_infos)):  
    # 새롭게 꺼낸 점
    curr_dot, curr_type, curr_width  = circle_infos[i]

    if curr_type == 'left':
        stack.append([curr_dot, 0])
    elif curr_type == 'right':
        start_dot, length_sum = stack.pop()
        curr_length = curr_dot - start_dot

        areas += 1
        if curr_length == length_sum:
            areas += 1

        if stack:
            stack[-1][1] += curr_length


print(areas)