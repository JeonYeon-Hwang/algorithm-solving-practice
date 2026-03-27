# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
import sys
from io import StringIO

file = """5"""


sys.stdin = StringIO(file)

input = sys.stdin.readline
N = int(input().rstrip())


# dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] ... dp[1] + 2
# 문제는 dp[i - 1] = dp[i -3] + dp[i - 4] .. dp[1] + 2
# 따라서 이를 요약하게 되면... => dp[i] = dp[i - 1] + dp[i - 2]

if N == 1:
    print(1)
elif N == 2:
    print(2)
elif N >= 3:
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, N + 1):
        temp = dp[i - 1] + dp[i -2]
        temp %= 15746
        dp[i] = temp 
    
    print(dp[N])

    