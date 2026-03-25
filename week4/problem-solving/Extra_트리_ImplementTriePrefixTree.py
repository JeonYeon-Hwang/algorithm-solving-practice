# 트리 - Implement Trie (Prefix Tree)
# 문제 링크: https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150


from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:



        return 1
    



if __name__ == "__main__":
    root = [-10, 9, 20, None, None, 15, 7]
    
    sol = Solution()
    result = sol.maxPathSum(root)
    
    print(f"결과: {result}")