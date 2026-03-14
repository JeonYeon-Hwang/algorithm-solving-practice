# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190
import sys
from collections import deque

try:
    sys.stdin = open('난이도중_큐_뱀_골드4.txt', 'r')
except FileNotFoundError:
    pass

N = int(input())
K = int(input())

apple_locations = set()
for i in range(K):
    temp = list(map(int, input().split(" ")))
    apple_locations.add(f"{temp[0] - 1}-{temp[1] - 1}")

# 뱀 마디 위치정보를 저장하는 큐
snake_queue = deque()
snake_queue.append([0, 0])

# 뱀의 방향 좌표를 저장하는 리스트
dir_idx = 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

is_game_over = False

# 특정 seconds 까지 뱀의 이동을 시뮬레이션 하는 함수
def simulate_snake_move(pre, cur):
    global is_game_over
    for i in range(pre, cur + 1):
        head_y, head_x = snake_queue[-1]
        # 뱀이 방향대로 감 
        head_y += direction[dir_idx][0]
        head_x += direction[dir_idx][1]

        # 범위에서 벗어났는지 판단
        if head_y < 0 or head_y >= N or \
            head_x < 0 or head_x >= N:
            print(i)
            is_game_over = True
            break
        # 뱀의 몸과 부딪히는지 판단 => 꼬리는 나중에 없어짐
        if [head_y, head_x] in snake_queue:
            print(i)
            is_game_over = True
            break
        
        # 몸통 충돌 여부 확인 후, 큐에 머리를 넣음
        snake_queue.append([head_y, head_x])  

        # 뱀이 사과를 먹었는지 판단
        if f"{head_y}-{head_x}" in apple_locations:
            apple_locations.remove(f"{head_y}-{head_x}")
            continue

        # 뱀의 꼬리는 빠짐
        snake_queue.popleft()


def turn_left():
    global dir_idx
    if dir_idx > 0:
        dir_idx -= 1
    else: 
        dir_idx = 3

def turn_right():
    global dir_idx
    if dir_idx < 3:
        dir_idx += 1
    else:
        dir_idx = 0


# 뱀 방향전환 명령어를 단계적 실행
pre_seconds = 0

D = int(input())
for i in range(D):
    if is_game_over:
        break
    
    # 뱀 직진 상황
    curr_seconds, change_dir = list(input().split(" "))
    simulate_snake_move(pre_seconds + 1, int(curr_seconds))
    pre_seconds = int(curr_seconds)
    
    # 방향을 변경함
    if change_dir == 'L':
        turn_left()
    elif change_dir == 'D':
        turn_right()


# 만약 무사히 뱀이 지나갔다면
while is_game_over is not True:
    simulate_snake_move(pre_seconds + 1, pre_seconds + 1)
    pre_seconds += 1