# 정수론 - Factorial Trailing Zeroes
# 문제 링크: https://leetcode.com/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)

        result = factorial(n)

        trailings = 0

        while result % 10 == 0:
            trailings += 1
            # print(f"{result} - {trailings}")
            result //= 10
        
        return trailings