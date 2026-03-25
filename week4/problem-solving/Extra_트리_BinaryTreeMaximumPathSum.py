# 트리 - Binary Tree Maximum Path Sum
# 문제 링크: https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150
import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    def __init__(self):
        self.max_sum = -math.inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:    
        self.dfs_sum(root)
        return self.max_sum

    def dfs_sum(self, node):
        if node.left is None and node.right is None:
            self.max_sum = max(self.max_sum, node.val)
            return node.val

        max_l = 0
        max_r = 0

        if node.left is not None:
            max_l = self.dfs_sum(node.left)
        if node.right is not None:
            max_r = self.dfs_sum(node.right)
        
        cutoff_sum = max_l + max_r + node.val
        self.max_sum = max(self.max_sum, cutoff_sum, node.val)
        
        push_up_val = max(node.val, node.val + max_l, node.val + max_r)
        self.max_sum = max(self.max_sum, push_up_val)
        
        return push_up_val
    


if __name__ == "__main__":
    root = TreeNode(-1)

    root.right = TreeNode(9)
    root.right.left = TreeNode(-6)
    root.right.right = TreeNode(3)

    root.right.right.right = TreeNode(-2)

    sol = Solution()
    result = sol.maxPathSum(root)
    
    print(f"결과: {result}")