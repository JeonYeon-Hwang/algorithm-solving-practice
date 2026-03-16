# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
import sys

try:
    sys.stdin = open('난이도중_해시테이블_세수의합_골드4.txt', 'r')
except FileNotFoundError:
    pass

ob = sys.stdin.readline
N = int(input().rstrip())
nums = []
hash_map = {}
sums = set()

for _ in range(N):
    input = sys.stdin.readline
    num = input().rstrip()
    nums.append(int(num))

nums.sort()

for a in nums:
    for b in nums:
        sums.add(a + b)

# 역순으로 검색
for i in range(N - 1, -1, -1):
    for j in range(i + 1):
        if nums[i] - nums[j] in sums:
            print(nums[i])
            exit()

            



