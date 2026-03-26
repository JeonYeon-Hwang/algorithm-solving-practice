# 그래프 - Course Schedule
# 문제 링크: https://leetcode.com/problems/course-schedule/?envType=study-plan-v2&envId=top-interview-150
from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
 
        in_degree = [0] * numCourses
        graph = {}
        q = deque()
        passed = 0

        for i in range(numCourses):
            graph[i] = []

        for a_i, b_i in prerequisites:
            graph[b_i].append(a_i)
            in_degree[a_i] += 1

        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            passed += 1

            for next in graph[curr]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    q.append(next)


        return True if passed == numCourses else False
    



if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0],[0,1]]

    sol = Solution()
    result = sol.canFinish(numCourses, prerequisites)
    
    print(f"결과: {result}")