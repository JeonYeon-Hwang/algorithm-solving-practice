# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
import sys
from io import StringIO

file = """2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
"""

sys.stdin = StringIO(file)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    rank_lst = []
    survived = N
    
    for _ in range(N):
        paper, meeting = map(int, input().split(' '))
        rank_lst.append((paper, meeting))

    rank_lst.sort(key=lambda x: x[0])

    pre = rank_lst[0][1]
    for i in range(1, N):
        cur = rank_lst[i][1]

        if pre < cur:
            survived -= 1
        elif pre > cur:
            pre = cur

    print(survived)