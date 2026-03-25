# 트리, BFS - Binary Tree Level Order Traversal
# 문제 링크: https://leetcode.com/problems/binary-tree-level-order-traversal/
from typing import List, Optional
from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque()
        q.append(root)

        lst = []

        while q:
            size = len(q)
            level = []

            for _ in range(size):
                cur = q.popleft()
                level.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            lst.append(level)

        return lst
    



if __name__ == "__main__":
    root = TreeNode(3)
    
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    sol = Solution()
    result = sol.levelOrder(root)
    
    print(f"결과: {result}")