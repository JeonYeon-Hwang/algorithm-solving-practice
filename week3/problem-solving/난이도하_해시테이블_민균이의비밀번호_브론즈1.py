# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
import sys

try:
    sys.stdin = open('난이도하_해시테이블_민균이의비밀번호_브론즈1.txt', 'r')
except FileNotFoundError:
    pass

input = sys.stdin.readline
N = int(input())
s = set()


def is_symmetry(word):
    if word == word[::-1]:
        return True
    else:
        return False
    

for i in range(N):
    keyword = input().rstrip()
    length = len(keyword)
    
    if keyword[::-1] in s:
        print(f"{length} {keyword[length // 2]}")
    
    if is_symmetry(keyword):   
        print(f"{length} {keyword[length // 2]}")
        break
    else:
        s.add(keyword)
    


