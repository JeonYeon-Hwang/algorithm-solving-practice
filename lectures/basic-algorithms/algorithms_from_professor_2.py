# 동인할 교수님이 격 주로 특강하러 오심
# 이분탐색 점화식 T(n) = T(n/2) + O(1) .. 이렇게 표현되는 이유가 뭘까..? => 이진탐샥애서 사용
# fast nultiplecation: xy = 10^2m + 10^m(bc + ad) + bc => bc + ad 

# 동적 프로그래밍 => 영리한 재귀로 불리기도 함(smart recursion)
# 피보나치 수열... 일반적인 재귀로는 계산 수가 기하 급숴적으로 증가함 => 배열을 이용하여 중복 계산을 줄임 .. 점화식을 찾는 것이 중요!

# grid에서 최단경로 갯수 세기... 
# 1. 먼저 base case 알아내기
# 2. 일반적인 경우의 점화식 찾기: P(i, j) = { 1 혹은 P(i - 1, j) + P(i, j - 1)}

# LCS... Longest Common Subsequence