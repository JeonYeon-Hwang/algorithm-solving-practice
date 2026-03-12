# 정수론 - Max Points on a Line
# 문제 링크: https://leetcode.com/problems/max-points-on-a-line/?envType=study-plan-v2&envId=top-interview-150

from typing import List
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_val = 0
        
        # y = kx + d 방정식 추출
        for i in range(len(points)):
            dictionary = {}
            duplicate = 0
            horizontal = 0
            vertical = 0

            for j in range(len(points)):
                a_y, a_x = points[i][0], points[i][1]
                b_y, b_x = points[j][0], points[j][1]

                dy = a_y - b_y
                dx = a_x - b_x

                if dy == 0 and dx == 0:
                    duplicate += 1
                    continue

                if dy == 0 and dx != 0:
                    vertical += 1
                    continue
                elif dy != 0 and dx == 0:
                    horizontal += 1
                    continue

                gcds = self.gcd(dy, dx)

                dy /= gcds
                dx /= gcds
                
                # 딕셔너리에 저장
                direction = "+" if dy * dx > 0 else "-"
                key = str(f"{direction}:{int(abs(dy))}:{int(abs(dx))}")
                dictionary[key] = dictionary.get(key, 0) + 1
            
            max_overlap = max(max(dictionary.values(), default=0), horizontal, vertical)
            max_val = max(max_val, max_overlap + duplicate)


        return max_val
        
    def gcd(self, a, b):
        a, b = abs(a), abs(b)
        if b == 0:
            return a
        
        def recursive(a, b):
            r = a % b
            if r == 0:
                return b
            return recursive(b, r)
        
        return recursive(a, b)




if __name__ == "__main__":
    # 데이터 준비
    points = [[1,1],[2,2],[3,3]]
    
    # 클래스 생성 및 실행
    sol = Solution()
    result = sol.maxPoints(points)
    
    # 결과 출력
    print(f"결과: {result}")