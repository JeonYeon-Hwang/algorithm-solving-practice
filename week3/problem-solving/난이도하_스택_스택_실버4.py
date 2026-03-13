# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
import sys


try:
    sys.stdin = open('난이도하_스택_스택_실버4.txt', 'r')
except FileNotFoundError:
    pass

N = int(input())
stack = []

for _ in range(N):
    input = sys.stdin.readline
    words = input().rstrip()
    commands = list(words.split(" "))
    command = commands[0]
    if command == 'push':
        stack.append(commands[1])
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])    
