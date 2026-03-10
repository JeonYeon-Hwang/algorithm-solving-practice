# 문자열 - 광고 (백준 플래4)
# 문제 링크: https://www.acmicpc.net/problem/1305

import sys


try:
    sys.stdin = open('난이도상_문자열_광고_플래4.txt', 'r')
except FileNotFoundError:
    pass

L = int(input())
pattern = input()
table = [0] * L

def kmp():
    j = 0
    for i in range(1, L):
        while j > 0 and pattern[i] != pattern[j]:   
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

kmp()

if table[L - 1] == 0:
    print(L)
else:
    print(L - table[L - 1])
