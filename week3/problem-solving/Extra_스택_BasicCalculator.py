# 스택 - Basic Calculator
# 문제 링크: https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150
import re

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        tokens = re.findall(r'\d+|[+-]|[()]', s)
        is_plus = True
        base_num = 0

        for i in range(len(tokens)):
            sign = tokens[i]
            
            if sign == '(':
                if is_plus: stack.append([0, 1])
                else: stack.append([0, -1])
                is_plus = True
                
            elif sign == ')':
                upper_val = stack.pop()
                val = upper_val[0] if upper_val[1] == 1 else -upper_val[0]
                if stack:
                    stack[-1][0] += val
                else: base_num += val
            else:
                # s가 숫자라면
                if sign.isalnum():
                    val = int(sign) if is_plus else -int(sign)
                    if stack:
                        stack[-1][0] += val
                    else:
                        base_num += val
                else:
                    if sign == '+': is_plus = True
                    elif sign == '-': is_plus = False

        return base_num


if __name__ == "__main__":
    str = "(1+(4+5+2)-3)+(6+8)"
    
    sol = Solution()
    result = sol.calculate(str)
    
    print(f"결과: {result}")