# 분할정복 - Construct Quad Tree
# 문제 링크: https://leetcode.com/problems/construct-quad-tree/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        node = Node(1, False, None, None, None, None)

        
        def divide_conquer(y, x, size):
            is_leaf = True
            first_color = grid[y][x]
            
            for i in range(y, y + size):      
                for j in range(x, x + size):
                    if first_color != grid[i][j]:
                        first_color = False
                        is_leaf = False
                        break
                if not is_leaf:
                    break

            if is_leaf:
                return Node(first_color, True, None, None, None, None)

            half = size // 2
            
            TopLeft = divide_conquer(y, x, half)
            TopRight = divide_conquer(y, x + half, half)
            BottomLeft = divide_conquer(y + half, x, half)
            BottomRight = divide_conquer(y + half, x + half, half)
            
            return Node(
                1, False,
                TopLeft, TopRight, BottomLeft, BottomRight
            )

        return divide_conquer(0, 0, n)
    

if __name__ == "__main__":
    grid = [[0,1],[1,0]]
    
    sol = Solution()
    result = sol.construct(grid)
    
    print(f"결과: {result}")