# 배열 - H-Index
# 문제 링크: https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hIndex = 0

        for i in range(len(citations)):
            if citations[i] < i + 1:
                break
            else:
                hIndex += 1
        
        return hIndex