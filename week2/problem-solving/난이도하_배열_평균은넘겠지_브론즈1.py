# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

import sys


try:
    sys.stdin = open('난이도하_배열_평균은넘겠지_브론즈1.txt', 'r')
except FileNotFoundError:
    pass

c = int(input())

while (True):
  sum = 0
  cnt = 0
  # 문자열 입력 받기
  str = input()

  # 학생들의 점수와 학생 수 분리
  strArr = str.split();
  studentNumber = int(strArr[0])
  del strArr[0]

  # 학생들의 점수 평균 구하기
  for score in strArr:
    sum += int(score)
    average = sum / studentNumber

  # 평균 이상인 학생들의 수 저장
  for i in range(studentNumber):
    if int(strArr[i]) > average:
      cnt += 1 

  # 평균 이상인 학생들의 비율을 소수점 셋째 자리까지 출력
  print(f"{(cnt / studentNumber) * 100:.3f}%")



  c -= 1
  if (c == 0):
    break