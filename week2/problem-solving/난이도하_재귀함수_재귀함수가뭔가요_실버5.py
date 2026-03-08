# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478

import sys


try:
    sys.stdin = open('난이도하_재귀함수_재귀함수가뭔가요_실버5.txt', 'r')
except FileNotFoundError:
    pass

recurse_num = int(input())
insert_pos = -1
add_depth = 4
add_on = '_'

quote = """어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
라고 답변하였지."""

repeating_quote = """"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
라고 답변하였지."""

final_quote = """"재귀함수가 뭔가요?"
"재귀함수는 자기 자신을 호출하는 함수라네"
라고 답변하였지."""

# 재귀 문구 삽입
for i in range(1, recurse_num):
    lines = quote.splitlines()
    insert_quote = "\n".join([f"{add_on * add_depth}{insert_lines}" for insert_lines in repeating_quote.splitlines()])
    lines.insert(insert_pos, insert_quote)
    quote = "\n".join(lines)

    add_depth += 4
    insert_pos -= 1

#최종 문구 처리
lines = quote.splitlines()    
final_quote = "\n".join([f"{add_on * add_depth}{final_line}" for final_line in final_quote.splitlines()])
lines.insert(insert_pos, final_quote)

print("\n".join(lines))