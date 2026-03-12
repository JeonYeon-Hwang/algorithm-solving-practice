# 배열 - Candy
# 문제 링크: https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies_go_right = [1] * len(ratings)
        candies_go_left = [1] * len(ratings)

        sums = 0

        if len(ratings) <= 1:
            return 1
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies_go_right[i] = candies_go_right[i - 1] + 1
            else:
                candies_go_right[i] = 1    

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies_go_left[i] = candies_go_left[i + 1] + 1
            else:
                candies_go_left[i] = 1

        
        for i in range(len(ratings)):
            sums += max(candies_go_right[i], candies_go_left[i])

        return sums