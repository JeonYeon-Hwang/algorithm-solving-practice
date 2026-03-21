# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
import sys

try:
    sys.stdin = open('난이도중_트리_이진검색트리_골드4.txt', 'r')
except FileNotFoundError:
    pass

sys.setrecursionlimit(100000)
input = sys.stdin.readline

pre_order = []

root = input().rstrip()
root = int(root)
pre_order.append(root)


while True:
    line = input().rstrip()

    if line == '':
        break
    
    pre_order.append(int(line))

# print(pre_order)

def divide(start, end):
    if start > end:
        return
    root = pre_order[start]
    split = end + 1

    for i in range(start + 1, end + 1):
        if pre_order[i] > root:
            split = i
            break

    divide(start + 1, split - 1)
    divide(split, end)
    print(root)  


end = len(pre_order)

divide(0, end - 1)