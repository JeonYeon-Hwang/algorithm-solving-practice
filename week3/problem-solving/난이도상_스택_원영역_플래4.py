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
s = set()
circle_infos = []

for _ in range(N):
    input = sys.stdin.readline
    lst = list(map(int, input().rstrip().split(" ")))
    x_left = lst[0] - lst[1]
    x_right = lst[0] + lst[1]
    diameters = abs(x_right - x_left)
    circle_infos.append([diameters, x_left, x_right])


circle_infos.sort(key=lambda x: x[0], reverse=True)
print(circle_infos)
# for i in range(len(circle_infos)):
