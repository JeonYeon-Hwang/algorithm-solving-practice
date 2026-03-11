# 백트래킹 - Word Search
# 문제 링크: https://leetcode.com/problems/word-search/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        delta = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        def journey(curr_y, curr_x, idx):      
            visited[curr_y][curr_x] = True
            idx += 1

            if idx == len(word):
                # print(f"{curr_y} {curr_x} 에서 종료")
                return True
            
            for dy, dx in delta:
                new_y = curr_y + dy
                new_x = curr_x + dx

                if new_y >= row or new_y < 0 or \
                    new_x >= col or new_x < 0:
                    continue

                if visited[new_y][new_x]:
                    continue

                if board[new_y][new_x] == word[idx]:
                    if journey(new_y, new_x, idx):
                        return True
                    visited[new_y][new_x] = False
            
            return False

                
        for y in range(row):
            for x in range(col):
                if board[y][x] == word[0]:
                    # print(f"{y},{x} 시작")
                    if journey(y, x, 0):
                        return True
                    visited[y][x] = False

        return False
    


if __name__ == "__main__":
    # 데이터 준비
    board = [["A", "A"]]
    word = "AA"
    
    # 클래스 생성 및 실행
    sol = Solution()
    result = sol.exist(board, word)
    
    # 결과 출력
    print(f"결과: {result}")

