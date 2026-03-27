# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
import sys
import re
from io import StringIO

file = """00009-00009"""


sys.stdin = StringIO(file)

input = sys.stdin.readline
expression = input().rstrip()
lst = re.findall(r'\d+|[+-]', expression)


# 그리디 알고리즘이라는데... 일단 뭔가 편애하는 규칙이 있을 듯.
# 개인적인 추정: - 를 최대한 늦게 계산하는 것이 최솟값인가?
# 다시 생각 => - 부호 뒤의 sum을 최대화 할 것.

lst_be_minus = [0]
begin = 0
be_minus = False
is_begin = True

for i in range(len(lst)):
    char = lst[i]

    if char.isdigit():
        num = int(char)

        if be_minus:
            lst_be_minus[-1] += num
        else:
            if is_begin:
                begin += num
            else:
                lst_be_minus.append(num)
                be_minus = True

    elif char == '-':
        be_minus = not be_minus
        is_begin = False

        
for num in lst_be_minus:
    begin -= num

print(begin)
