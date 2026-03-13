# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
import sys


try:
    sys.stdin = open('난이도하_분할정복_색종이만들기_실버2.txt', 'r')
except FileNotFoundError:
    pass

N = int(input())
paper_map = []

while N > 0:
    cols = list(map(int, input().split()))
    paper_map.append(cols)
    N -= 1

def find_paper(y_left, y_right, x_left, x_right):

    if is_one_paper(y_left, y_right, x_left, x_right):
        return

    y_mid = (y_left + y_right) // 2
    x_mid = (x_left + x_right) // 2

    # 1사분면
    find_paper(y_left, y_mid, x_mid + 1, x_right)
    # 2사분면
    find_paper(y_left, y_mid, x_left, x_mid)
    # 3사분면
    find_paper(y_mid + 1, y_right, x_left, x_mid)
    # 4사분면
    find_paper(y_mid + 1, y_right, x_mid + 1, x_right)



def is_one_paper(y_left, y_right, x_left, x_right):
    global blue_papers, white_papers

    begin_color = paper_map[y_left][x_left]
    
    if y_left == y_right:
        if begin_color == 1:
            blue_papers += 1 
        else:
            white_papers += 1
        return True

    for y in range(y_left, y_right + 1):
        for x in range(x_left, x_right + 1):
            if paper_map[y][x] != begin_color:
                return False
    
    if begin_color == 1:
        blue_papers += 1 
    else:
        white_papers += 1
    return True

n = len(paper_map) - 1
blue_papers = 0
white_papers = 0

find_paper(0, n, 0, n)
print(white_papers)
print(blue_papers)