# 큐 - 가운데를 말해요 (백준 골드2)
# 문제 링크: https://www.acmicpc.net/problem/1655
import sys
import heapq

try:
    sys.stdin = open('난이도상_큐_가운데를말해요_골드2.txt', 'r')
except FileNotFoundError:
    pass

ob = sys.stdin.readline
N = int(input().rstrip())

pq = []
nums_asc = []
nums_which_pushed = []

for i in range(N):
    input = sys.stdin.readline
    num = int(input().rstrip())
    heapq.heappush(pq, (num, i))
    nums_which_pushed.append(num)


pq_idx = 0
while pq:
    num, when_it_pushed = heapq.heappop(pq)
    pq_idx += 1
    nums_asc.append(num)

a_sac = []
b_sac = []

heapq.heappush(a_sac, -nums_which_pushed[0])
print(nums_which_pushed[0])

if N <= 1:
    pass

if -a_sac[0] > nums_which_pushed[1]:
    a_max = heapq.heappop(a_sac)
    heapq.heappush(b_sac, -a_max)
    heapq.heappush(a_sac, -nums_which_pushed[1])
else:
    heapq.heappush(b_sac, nums_which_pushed[1])

print(-a_sac[0])

if N <= 2:
    pass

for i in range(2, N):
    new_num = nums_which_pushed[i]
    b_sac_min = b_sac[0] 
    a_sac_max = -a_sac[0] 

    if new_num >= b_sac_min:
        heapq.heappush(b_sac, new_num)
    else:
        heapq.heappush(a_sac, -new_num)

    a_len = len(a_sac)
    b_len = len(b_sac)

    if b_len > a_len:
        b_min = heapq.heappop(b_sac)
        heapq.heappush(a_sac, -b_min)
    elif a_len > b_len + 1:
        a_max = heapq.heappop(a_sac)
        heapq.heappush(b_sac, -a_max)

    print(-a_sac[0])



