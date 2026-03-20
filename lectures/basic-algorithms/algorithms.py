# 강의자: 이동석 코치
# recursion에 대한 설명
# 프로그래밍의 요소 => primitive expressions, means of combination, means of abstraction(추상화.. 중요!) => 요 세가지 만으로 복잡한 일을 수행할 수 있음
# 추상화란... 일종의 계층화 된 곳에서 단계의 지점인가?

# 함수를 일단 짜 보라고 하심
def nsum(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

# 이 위와 같은 방식은 iteration이라고 부른다(첫 번째부터 n까지 순회)
# 이제 재귀함수로 이를 만들어보자
def sum(n):
    return n + sum(n - 1)

# 위의 방식은 무한 루프에 빠지게 된다. 
# 결국 탈출을 하기 위해 base case를 넣어야 함 - 여기서 마치 '부매랑' 처럼 '변곡점'을 찍고 돌아옴

def sum_with_basecase(n):
    # base condition
    if n == 0:
        return 0
    return n + sum(n - 1)

# recursion은 중간에 break 하면 값을 얻을 수 없음
# 이번에는 좀 다른 형태의 recursion을 보자 - tail recursion:

def sum_iter(n, total):
    if n == 0:
        return total

    else:
        return sum_iter(n - 1, total + n)
    
def sum_tail_recursion(n):
    return sum_iter(n, 0)

# 얘는 부매랑 처럼 돌지 않음, 중간 단계 얻을 수 있음, for 문과 유사?


# 요 코드를 구현해 보라고 하심:
def expt(b, n):
    if n == 0:
        return 1
    return b * expt(b, n - 1)

# fast exponentiation 구현하기:
# fast exponentiation - iteration
# 피보나치 수열...

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# recursion은 오버헤드가 심하기 때문에... 어떻게 최적화 하는 방법이 없을까? 생각.
# 이런 형태는 tree-recursion이라 한다
# 하노이 탑 문제 -- 대표적인 recursion 문제.