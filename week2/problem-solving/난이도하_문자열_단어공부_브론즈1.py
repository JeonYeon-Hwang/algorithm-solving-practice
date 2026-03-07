# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

import sys


try:
    sys.stdin = open('난이도하_문자열_단어공부_브론즈1.txt', 'r')
except FileNotFoundError:
    pass

word = input()
word = word.upper()

list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

max_count = 0
max_char = ''

for char in list:
    count_c = word.count(char)
    if max_count < count_c:
        max_char = char
        max_count = count_c
    elif max_count == count_c:
        max_char = '?'

print(max_char)

