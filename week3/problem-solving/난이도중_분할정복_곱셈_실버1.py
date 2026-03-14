# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
import sys


try:
    sys.stdin = open('난이도중_분할정복_곱셈_실버1.txt', 'r')
except FileNotFoundError:
    pass

lst = list(map(int, input().split(" ")))
num = lst[0]
n = lst[1]
last = lst[2]

def divide_conquer(num, n, last):
    if n == 1:
        return (num ** n) % last
    
    temp = divide_conquer(num, n // 2, last)
    
    if n % 2 == 0:
        return (temp * temp) % last
    else:
        return (temp * temp * num) % last

print(divide_conquer(num, n, last))





